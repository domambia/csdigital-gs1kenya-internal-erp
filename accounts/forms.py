from django import forms
from django.contrib.auth.models import User
from accounts.models import Employee
from bootstrap_datepicker_plus import DatePickerInput

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    email = forms.CharField(widget = forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'password', 'first_name')

    def _str__(self):
        return self.username



class EmployeeForm(forms.ModelForm):
    phone = forms.CharField(widget = forms.NumberInput())
    date_of_birth = forms.DateField(
            widget=DatePickerInput(format='%m/%d/%Y')
        )
    salary = forms.CharField(widget = forms.NumberInput())
    class Meta:
        model = Employee
        fields = ('address', 'phone', 'date_of_birth',
        'county', 'dependant_name', 'dependant_contact', 'dependant_relationship',
        'position', 'department', 'salary', 'kin_email')
