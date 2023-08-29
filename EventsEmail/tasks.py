from celery import shared_task
from django.core.mail import send_mail
from .models import Event,EmailTemplate, EmailLog
from django.db.models import Q
from datetime import date
from django.template import Template, Context


@shared_task
def send_event_emails():
    # Get today's date
    today = date.today()

    # Get upcoming birthday and work anniversary events
    upcoming_events = Event.objects.filter(
        Q(event_type='Birthday', event_date__month=today.month, event_date__day=today.day) |
        Q(event_type='Work Anniversary', event_date__month=today.month, event_date__day=today.day)
    )
    if not upcoming_events:
        # Log that no events are scheduled
        log_message = "No events are scheduled for the current period."
        EmailLog.objects.create(message=log_message)  # Create a log entry
        print(log_message)

    else:
        for event in upcoming_events:
            employee = event.employee
            event_type = event.event_type
            event_date = event.event_date
            years_worked = event_date.year - employee.start_date.year  # Calculate work anniversary years

            # Retrieve corresponding email template
            email_template = EmailTemplate.objects.get(event_type=event_type)

            # Populate the email template using Django's template system
            template = Template(email_template.template_content)
            context = Context({
                'name': employee.name,
                'years': years_worked if event_type == 'Work Anniversary' else None,
                'event_type': event_type
            })
            template_content = template.render(context)
            try:
                # Send the email
                send_mail(
                    subject=f"Event: {event_type}",
                    message="",
                    from_email='sender@gmail.com',
                    recipient_list=[employee.email],
                    html_message=template_content
                )
                # Log successful email
                EmailLog.objects.create(event=event, status='Successful')
            except Exception as e:
                # Log failed email
                EmailLog.objects.create(event=event, status='Failed', message=str(e))



