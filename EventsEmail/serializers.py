from rest_framework import serializers
from .models import Employee, Event,EmailTemplate,EmailLog

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()  # Use the EmployeeSerializer for the ForeignKey
    class Meta:
        model = Event
        fields = ('event_type', 'event_date', 'employee')

class EmailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = '__all__'

class EmailLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLog
        fields = '__all__'