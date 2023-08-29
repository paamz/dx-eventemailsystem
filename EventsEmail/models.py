from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=70)
    emp_email = models.EmailField(unique=True)

class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    event_date = models.DateField()

class EmailTemplate(models.Model):
    event_type = models.CharField(max_length=50, unique=True)
    template_content = models.TextField()

class EmailLog(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)  # Successful, Failed, Retry
    message = models.TextField(blank=True)
