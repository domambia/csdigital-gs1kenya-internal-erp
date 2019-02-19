from django.shortcuts import render
from django.contrib.auth.models import User 
from accounts.models import Employee
# Create your views here.

def dashboard(request):
    current = User.objects.get(username = request.session['username'])
    employee = Employee.objects.get(user = current.id)
    return render(request, "accnts/dashboard.html", {"employee": employee })