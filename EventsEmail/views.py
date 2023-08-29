from django.shortcuts import render
from rest_framework import status

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, Event,EmailTemplate,EmailLog
from .serializers import EmployeeSerializer,EventSerializer,EmailTemplateSerializer,EmailLogSerializer
from rest_framework.views import APIView

# To show the list of employee
@api_view(['GET'])
def employees_list(request):
    employees_queryset = Employee.objects.all()
    serializer = EmployeeSerializer(employees_queryset, many=True)
    return Response(serializer.data)

# since we can show the list of events
@api_view(['GET'])
def event_list(request):
    event_queryset = Event.objects.select_related('employee')
    ev_serializer = EventSerializer(event_queryset,many=True)
    return Response(ev_serializer.data)

# to show the templates
@api_view(['GET'])
def email_template_list(request):
    templates = EmailTemplate.objects.all()
    serializer = EmailTemplateSerializer(templates, many=True)
    return Response(serializer.data)

# fetch logs for admin
@api_view(['GET'])
def email_log_list(request):
    logs = EmailLog.objects.all()
    serializer = EmailLogSerializer(logs, many=True)
    return Response(serializer.data)

# apart from the admin panel if we want to insert data by API
# this class/method allows us to insert employee data using API
class Events(APIView):
    @api_view(['POST'])
    def add_employee(request):
        if request.method == 'POST':
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)