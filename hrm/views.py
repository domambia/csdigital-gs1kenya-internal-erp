from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from accounts.models import Employee
from leave.models import ApplyLeave 
from departments.models import Department, Position 
from django.contrib.auth.models import User 
# Create your views here.

def index(request):
    applied_leaves = ApplyLeave.objects.count()
    employees = Employee.objects.count()
    positions = Position.objects.count()
    departments = Department.objects.count()
    user = User.objects.get(username = request.session['username'])
    employee = Employee.objects.get(user = user.id)

    return render(request, "hrm/dashboard.html", 
                    {'employees': employees, 'positions': positions, 'departments': departments,
                     'applied_leaves': applied_leaves, "employee": employee, "user":user})


