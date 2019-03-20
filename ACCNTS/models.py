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
class Payment(models.Model):
    OPTIONS = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    PAYMENT = (
        ("Membership", "Membership"),
        ("Renewal", "Renewal"),
        ("Others", "Others"),
    )
    member = models.ForeignKey(Client, on_delete = models.CASCADE, default = 1)
    description = models.CharField(max_length = 1000)
    payment_for = models.CharField(max_length = 100, choices = PAYMENT, default = "Membership")
    date_of_generate = models.DateField(default = datetime.datetime.now)
    VAT = models.CharField(max_length = 5, choices = OPTIONS, default = "No")
    amount = models.PositiveIntegerField(blank = True, default = 0)

    def get_absolute_url(self):
        return reverse("ACCNTS:payment_list")

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
'''
Sales models
'''

class Sales(models.Model):
    member = models.ForeignKey(Client, on_delete = models.CASCADE, default = 1)
    invoice = models.ForeignKey(Invoice, on_delete = models.CASCADE, default = 1)
    amount_paid = models.IntegerField(default = 0)
    payment_due = models.DateField(default =datetime.datetime.now)
    payment_terms = models.CharField(max_length = 200)
    date_of_sale = models.DateField(default = datetime.datetime.now)

    def __str__(self):
        return member.company_name

    def get_absolute_url(self):
        return reverse("ACCNTS:sales_list")


