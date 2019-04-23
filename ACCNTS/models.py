from django.db import models
from CRM.models import Client
import datetime
from accounts.models import Employee
import datetime
from CRM.models import Supplier, Member
from django.urls import reverse
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
    pension = models.IntegerField(default=0)
    lunch = models.IntegerField(default=0)
    month = models.DateField(default = datetime.datetime.now)
    is_taxed = models.BooleanField(default = False)
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
        return "Sales"

    def get_absolute_url(self):
        return reverse("ACCNTS:sales_list")


'''
Expenses Types'''
def expenses_types():
    types = ['Operational', 'Financial', 'Administrative']
    list_of_types = []
    for x in types:
        list_of_types.append((x.lower(), x.capitalize()),)
        return tuple(list_of_types)
'''
Methods of payment'''
def method_of_payment():
    methods = ['Mpesa', 'Bank Cheque', 'Cash',]
    list_methods = []
    for method in methods:
        list_methods.append((method.lower(), method.capitalize()),)
    return tuple(list_methods)

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
    amount = models.PositiveIntegerField(default = 0)
    expense_type = models.CharField(max_length = 100, choices = expenses_types(), default = 'operational')

    def __str__(self):
        self.vendor.name

    def get_absolute_url(self):
        return reverse("ACCNTS:expense_list")


'''
Accounts models:
   Assets, Liability, Income,Expenses
'''
def assets_type():
    assests = ['Current', 'Fixed']
    list_asset = []
    for y in assests:
        list_asset.append((y.lower(), y.capitalize()))
    return tuple(list_asset)

class Asset(models.Model):
    name = models.CharField(max_length =500)
    type = models.CharField(max_length = 200, choices = assets_type(), default = 'current')
    open_balance = models.IntegerField(default = 0, blank = True)
    amount = models.IntegerField(default = 0)
    memo  = models.CharField(max_length = 200)
    dated = models.DateField(default = datetime.datetime.now)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("ACCNTS:asset_list")

def income():
    income = ['other incomes', 'direct income',]
    income_list = []
    for y in income:
        income_list.append((y.lower(), y.capitalize()))
    return tuple(income_list)


class Income(models.Model):
    name = models.CharField(max_length = 200)
    member = models.ForeignKey(Member, on_delete = models.CASCADE, default = 1)
    type = models.CharField(max_length = 200, choices = income(), default = 'direct income')
    amount = models.IntegerField(default = 0)
    open_balance = models.IntegerField(default = 0, blank = True)
    memo = models.CharField(max_length = 200)
    dated = models.DateField(default = datetime.datetime.now)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ACCNTS:income_list")

def liability():
    liab = ['current', 'short-term',]
    liab_list = []
    for y in liab:
        liab_list.append((y.lower(), y.capitalize()))
    return tuple(liab_list)


class Liability(models.Model):
    name = models.CharField(max_length = 200)
    type = models.CharField(max_length = 100, choices = liability(), default = 'current')
    amount = models.IntegerField(default = 0)
    open_balance = models.IntegerField(default = 0, blank = True)
    memo = models.CharField(max_length = 200)
    dated = models.DateField(default = datetime.datetime.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ACCNTS:liability_list")



'''
Banking Model'''
class Bank(models.Model):
    OPTIONS = (
        ('Payment', 'Payment'),
        ('Sales Receipt', 'Sales reciept'),
    )
    type = models.CharField(max_length = 50, choices = OPTIONS, default='Payment')
    ref_number = models.CharField(max_length = 100)
    dated = models.DateField(default = datetime.datetime.now)
    name = models.CharField(max_length=200)
    banked = models.CharField(max_length = 200)
    amount = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ACCNTS:bank_list")


"""
Deductions from the payroll

"""
#Deduction(employee = emp_id, nssf = nssf, nhif=nhif, nhsb= nhe, paye = tax)
class Deduction(models.Model):
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    nssf = models.IntegerField()
    nhif = models.IntegerField()
    nhsb = models.IntegerField()
    paye = models.IntegerField()
    dated = models.DateTimeField(default  = datetime.datetime.now)

    def __str__(self):
        return "Tax"













