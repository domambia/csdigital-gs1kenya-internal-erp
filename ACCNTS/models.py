from django.db import models
from CRM.models import Client
import datetime
from django.urls import reverse
from accounts.models import Employee
import datetime
# Create your models here.

class Invoice(models.Model):
    OPTIONS =(
        ("Yes", "Yes"),
        ("No", "No"),
    )
    member = models.ForeignKey(Client, on_delete = models.CASCADE,  default = 1)
    date_of_generate = models.DateField(default = datetime.datetime.now)
    description = models.CharField(max_length=2000)
    VAT = models.CharField(max_length = 5, choices = OPTIONS, default = "No")
    amount = models.PositiveIntegerField(blank=True, default=0)
    balance = models.PositiveIntegerField(blank=True, default=0) 
    def __str__(self):
        return self.member.company_name

    def get_absolute_url(self):
        return reverse("ACCNTS:list_profoma")



'''
PayRoll Model
'''
class PayRoll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=1)
    transport_allowance = models.IntegerField(default=0)
    leave_allowance = models.IntegerField(default=0)
    hse_allowance = models.IntegerField(default=0)
    loans = models.IntegerField(default=0)
    other_deductions = models.IntegerField(default=0)
    month = models.DateField(default = datetime.datetime.now)
    def __str__(self):
        return self.employee.user.username

    def get_absolute_url(self):
        return reverse("ACCNTS:list_payroll")
