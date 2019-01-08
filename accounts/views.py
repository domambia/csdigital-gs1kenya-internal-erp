from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import UserForm, EmployeeForm
from accounts.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView

"""List
"""
@login_required
def index(request):

    users_details = Employee.objects.select_related('user')

    return render(request, "hrm/index.html",
                  {'users': users_details,})

"""Add New Employee Information
This includes the login Information
"""
@login_required
def add_employee(request):
    u = User.objects.all()

    user_form = UserForm(request.POST or None)
    employee_form = EmployeeForm(request.POST or None)
    if request.method == 'POST':

        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save(commit = False)
            password = user_form.cleaned_data['password']
            print(password)
            user.set_password(password)
            user.save()

            employee = employee_form.save(commit = False)

            employee.user = user
            employee.save()
            return HttpResponseRedirect(reverse('hrm:hrm_index'))
        else:
            print(user_form.errors)
            print(employee_form.errors)
            return render(request, "employee/register.html",
                                {'user_form': user_form, 'employee_form': employee_form,})

    return render(request, "employee/register.html",
                        {'user_form': user_form, 'employee_form': employee_form,})


"""LOGIN: All User
"""
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session.session_key
                request.session['username'] = username
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is not activated. Please check your email account")
        else:
            print("Somone tried To  login and Failed")
            print("Username: {} with a Password: {}".format(username, password))
            return HttpResponseRedirect(reverse('index'))

    return render(request, "accounts/login.html", {})

"""LOGOUT: Module
"""

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


"""CRUD Operations: Delete, Update
"""

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('accounts:index')
    return render(request, "accounts/delete.html", {'employee': employee})


"""Update View
"""


def employee_update(request, pk):
    employee_form = EmployeeForm(request.POST or None,
                    instance = get_object_or_404(Employee, pk=pk))
    if request.method == "POST":
        if employee_form.is_valid():
            employee = employee_form.save()
            return HttpResponseRedirect(reverse('accounts:index'))
    return render(request, "accounts/edit.html",
                    {'employee_form': employee_form,})


""" EMPLOYEES PROFILE
    This enables one to access his or her own profile details
    An Employee can be able to edit his or her record(s)
"""

class EmployeeDetailView(DetailView):
    context_object_name = "employee"
    fields = ('username', 'email', 'first_name', 'last_name','salary',
              'phone')
    model = Employee
    template_name = "accounts/employee_detail.html"
