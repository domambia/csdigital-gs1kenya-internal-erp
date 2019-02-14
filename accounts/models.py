from django.db import models
from django.contrib.auth.models import User
from departments.models import Position, Department
from helpers.help import get_country
from django.urls import reverse



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional attributes for the employee

    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    date_of_birth = models.CharField(max_length=20)
    next_of_kin_name = models.CharField(max_length=60, blank=True)
    alt_phone_number = models.IntegerField(default = 0)
    # more
    kin_email = models.CharField(max_length=100, blank=True, unique = True)
    county = models.CharField(max_length=100,  blank=True, choices = get_country(), default = "No country")
    next_of_kin_phone = models.CharField(max_length=20, blank=True)

    # Dependants info
    dependant_name = models.CharField(max_length=100, blank=True)
    dependant_relationship = models.CharField(max_length=60, blank=True)
    dependant_contact = models.CharField(max_length=60, blank=True)
    leave_balance = models.IntegerField(default= 30)
    leave_bal = models.IntegerField(default= 4)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)
    company_benifits = models.CharField(max_length = 1000, default = "Pay NHIF, NSSF")

    # Job Information
    position = models.ForeignKey(Position, on_delete =models.CASCADE, default = 0)

    # Salary Information
    salary = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return (self.user.first_name + " " +self.user.last_name)

    def get_absolute_url(self):
    
        return reverse("accounts:employees")


