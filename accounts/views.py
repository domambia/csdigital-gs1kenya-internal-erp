from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import UserForm, EmployeeForm
from accounts.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, UpdateView
from django.core.mail import send_mail
from helpers.help import get_country

"""List
"""

@login_required
def index(request):
    current_user = User.objects.get(username = request.session['username'])
    users_details = Employee.objects.select_related('user')
    employee = Employee.objects.get(user = current_user.id)
    return render(request, "hrm/index.html",
                  {'users': users_details, "employee": employee})

"""Add New Employee Information
This includes the login Information
"""
@login_required
def add_employee(request):
    u = User.objects.all()
    countries = get_country()
    user_form = UserForm(request.POST or None)
    employee_form = EmployeeForm(request.POST or None)
    emp = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    if request.method == 'POST':

        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save(commit = False)
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()

            employee = employee_form.save(commit = False)

            employee.user = user
            if 'profile_pic' in request.FILES:
                employee.profile_pic = request.FILES['profile_pic']
            employee.save()
            return HttpResponseRedirect(reverse('accounts:employees'))
        else:
            return render(request, "accounts/register.html",
                                {'user_form': user_form, 'employee_form': employee_form, "countries": countries,"employee":emp,})

    return render(request, "accounts/register.html",
                        {'user_form': user_form, 'employee_form': employee_form, "countries": countries,"employee":emp,})


"""LOGIN: All User
"""
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username').lower()

        password = request.POST.get('password').lower()

        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)
                request.session.session_key
                if '@' in username:
                    print("Yes Omambia")
                    request.session['username'] = User.objects.get(email = username).username
                else:
                    request.session['username'] = username
                return HttpResponseRedirect(reverse('index'))
            elif request.user.is_authenticated():
                HttpResponseRedirect(reverse('index'))
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
    emp = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    if request.method == "POST":
        employee.delete()
        return redirect('accounts:employees')
    return render(request, "accounts/delete.html", {'emp': emp, "employee": employee})


"""Update View
"""

class EmployeeUpdateView(UpdateView):
    fields = ('address', 'phone', 'date_of_birth',
        'county', 'dependant_name', 'dependant_contact', 'dependant_relationship',
        'position', 'salary', 'kin_email', 'alt_phone_number', 'profile_pic', 'company_benifits')
    model = Employee
    template_name  = "accounts/edit.html"
    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context

""" EMPLOYEES PROFILE
    This enables one to access his or her own profile details
    An Employee can be able to edit his or her record(s)
"""

class EmployeeDetailView(DetailView):
    context_object_name = "user_info"
    model = Employee
    template_name = "accounts/employee_detail.html"
    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context
'''
Edit User authentications information
'''
def edit_authentications(request, pk):
    form = UserForm(request.POST or None, instance=get_object_or_404(User, pk=pk))
    current_user = User.objects.get(id = pk)
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit = False)
            user.username  = form.cleaned_data['username'].lower()
            user.email  = form.cleaned_data['email'].lower()
            user.set_password(form.cleaned_data['password'])
            user.save()
            logout(request)
            return HttpResponseRedirect(reverse('index'))
    return render(request, "accounts/auth.html", {'employee': employee, 'form': form})


