from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from accounts.models import Employee
from leave.models import ApplyLeave 
from departments.models import Department, Position 
# Create your views here.

def index(request):
    applied_leaves = ApplyLeave.objects.count()
    employees = Employee.objects.count()
    positions = Position.objects.count()
    departments = Department.objects.count()

    return render(request, "hrm/dashboard.html", 
                    {'employees': employees, 'positions': positions, 'departments': departments, 'applied_leaves': applied_leaves})


