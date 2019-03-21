from django.db import models
from CRM.models import Client
import datetime
from django.urls import reverse
from accounts.models import Employee
import datetime
from CRM.models import Supplier
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
    payment_due = models.DateField(default =datetime.datetime.now)
    payment_terms = models.CharField(max_length = 200)
    date_of_sale = models.DateField(default = datetime.datetime.now)

    def __str__(self):
        return member.company_name

    def get_absolute_url(self):
        return reverse("ACCNTS:sales_list")


'''
Expenses Types'''
def expenses_types():
    types = ['Operational', 'Financial', 'Administrative']
    list_of_types = []
    for x in types:
        list_of_types.append((x.lower(), x.capitalize()),)
        return tupe(list_of_types)
'''
Methods of payment'''
def method_of_payment():
    methods = ['Mpesa', 'Bank Cheque', 'Cash',]
    list_methods = []
    for method in methods:
        list_methods.append((method.lower(), method.capitalize()),)
    return tupe(list_methods)

def VAT():
    vat = ['Yes', 'No']
    vat_list = []
    for x in vat:
        vat_list.append((x.lower(), x.capitalize()),)
    return tuple(vat_list)

def get_terms():
    terms  = ['Pay immediately', 'Bill in 10 days', 'Bill in 20 days', 'Bill in 30 days', 'Bill in 60 days']
    terms_list = []
    for term  in terms:
        terms_list.append((term.capitalize(), term.capitalize()),)
    return tuple(terms_list)

class Expense(models.Model):
    vendor = models.ForeignKey(Supplier, on_delete = models.CASCADE, default = 1)
    date_of_expense  = models.DateField(default = datetime.datetime.now)
    memo = models.CharField(max_length = 1000)
    bill_due = models.DateField(default = datetime.datetime.now)
    terms_of_payment = models.CharField(max_length = 100, choices = get_terms(), default = "Pay Immediately")
    payment_method = models.CharField(max_length = 200, choices = method_of_payment(), default = "Bank Cheque")
    VAT = models.CharField(max_length = 10, choices = VAT(), default = "yes")
    ref_no = models.CharField(max_length = 100, blank = True)
    amount = models.PositiveInteger(default = 0)
    expense_type = models.CharField(max_length = 100, choices = expense_type(), default = 'operational')

    def __str__(self):
        self.vendor.name

    def get_absolute_url(self):
        return reverse("")


