from django.urls import path
from .views import employees_list, event_list,email_template_list,email_log_list
from .views import Events

urlpatterns = [
    path('api/employees', employees_list, name='employee-list'),
    path('api/events', event_list, name='event-list'),
    path('api/templates', email_template_list, name='template-list'),
    path('api/logs', email_log_list, name='log-list'),

    # Post url used to create employee records
    path('api/add_employee',Events.add_employee,name='Create Employee Data')
]