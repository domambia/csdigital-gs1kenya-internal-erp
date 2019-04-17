from django.db import models
from django.contrib.auth.models import User
from departments.models import Position, Department
from helpers.help import get_country
from django.urls import reverse
from django.core.validators import  MinValueValidator, EmailValidator


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional attributes for the employee
    address = models.CharField(max_length=50, blank=True)
    phone = models.IntegerField(validators=[MinValueValidator(9)])
    date_of_birth = models.CharField(max_length=20)
    huduma = models.CharField(max_length =50, default = "HUD-001232")
    id_no = models.IntegerField(default = 0)
    nssf_no = models.CharField(default = "NSSF_NO", max_length = 50)
    nhif_no = models.CharField(default = "NHIF_NO", max_length = 50)
    KRA = models.CharField(default = "KRA_PIN", max_length = 50)
    employee_no = models.CharField(default = 'GS1_NO', max_length=50)
    bank = models.IntegerField(default = 123456)
    next_of_kin_name = models.CharField(max_length=60, blank=True)
    alt_phone_number = models.IntegerField(validators=[ MinValueValidator(9)], blank = True)
    # more
    kin_email = models.CharField(max_length=100, blank=True, unique = True, validators=[ EmailValidator("Enter a valid email address")])
    county = models.CharField(max_length=100,  blank=True, choices = get_country(), default = "Kenya")
    next_of_kin_phone = models.CharField(max_length=20, blank=True)
    # Dependants info
    dependant_name = models.CharField(max_length=100, blank=True)
    dependant_relationship = models.CharField(max_length=60, blank=True, )
    dependant_contact = models.CharField(max_length=60, blank=True)
    leave_bal = models.PositiveIntegerField(default= 21, blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)
    company_benifits = models.CharField(max_length = 1000, default = "NSSF", blank = True)
    position = models.OneToOneField(Position, on_delete =models.CASCADE, default= 1)

    # Salary Information
    salary = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return (self.user.first_name + " " +self.user.last_name)

    def get_absolute_url(self):
        return reverse("accounts:employees")



