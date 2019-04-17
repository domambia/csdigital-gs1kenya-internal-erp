from ACCNTS.models import Sales, Bank, Expense, Liability, Asset, Income, Deduction
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import datetime
from django.contrib.auth.models import User
from accounts.models import Employee
from django.db.models import Sum
from django.contrib import messages
from django.http import HttpResponseRedirect
from helpers.help import check_user_login
from django.urls import reverse
from django.db.models import Q
'''
Sales Report'''

def sales_report(request):
    if not request.session.get('username'):
        messages.info(request, "Please login again to continue.")
        return HttpResponseRedirect(reverse("accounts:login"))
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    if request.method == "POST":
        start  = request.POST['start']
        end = request.POST['end']
        print("The date is coming.{}".format(start))
        sales = Sales.objects.filter(date_of_sale__range = [start, end])
        type(sales)
        #total = Sales.objects.filter(date_of_sale__range =[start, end]).aggregate(Sum('amount'))
        #print(total)
        return render(request, "reports/sales_report.html", {'sales': sales,'start': start,
                'end': end, 'employee': employee })
    return render(request, "reports/sales_report.html", {'employee': employee,'start': 'select date',
                'end': 'select date', 'sales': []})

def expenses_report(request):
    if not request.session.get('username'):
        messages.info(request, "Please login again to continue.")
        return HttpResponseRedirect(reverse("accounts:login"))
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    if request.method == "POST":
        start  = request.POST['start']
        end = request.POST['end']
        results = Expense.objects.filter(date_of_expense__range = [start, end])
        total = Expense.objects.filter(date_of_expense__range =[start, end]).aggregate(Sum('amount'))
        print("ksh."+ str(total['amount__sum']))
        return render(request, "reports/expense_report.html", {'results': results,'start': start,
                'end': end, 'employee': employee, "total": total['amount__sum'] })
    return render(request, "reports/expense_report.html", {'employee': employee, 'start': 'select date',
                'end': 'select date', 'results': [],  "total": 0})

'''
Banking Details Reports'''
def banking_report(request):
    if not request.session.get('username'):
        messages.info(request, "Please login again to continue.")
        return HttpResponseRedirect(reverse("accounts:login"))
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    if request.method == "POST":
        start  = request.POST['start']
        end = request.POST['end']
        results = Bank.objects.filter(dated__range = [start, end])
        total = Bank.objects.filter(dated__range =[start, end]).aggregate(Sum('amount'))
        return render(request, "reports/banking_report.html", {'banks': results, 'start': start,
                'end': end, 'employee': employee, "total": total['amount__sum'] })
    return render(request, "reports/banking_report.html", {'employee': employee, 'start': 'select date',
                'end': 'select date', 'banks': [],  "total": 0})


'''
Banking Details Reports'''
def fixed_asset_report(request):
    if not request.session.get('username'):
        messages.info(request, "Please login again to continue.")
        return HttpResponseRedirect(reverse("accounts:login"))
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    if request.method == "POST":
        start  = request.POST['start']
        end = request.POST['end']
        results = Asset.objects.filter(dated__range = [start, end])
        print(results)
        total = Asset.objects.filter(dated__range =[start, end]).aggregate(Sum('amount'))
        return render(request, "reports/asset_report.html", {'assets': results, 'start': 'select date',
                'end': 'select date', 'employee': employee, "total": total['amount__sum'] })
    return render(request, "reports/asset_report.html", {'employee': employee, 'assets': [],  "total": 0})

'''
Banking Details Reports'''
def profit_and_loss_report(request):
    if not request.session.get('username'):
        messages.info(request, "Please login again to continue.")
        return HttpResponseRedirect(reverse("accounts:login"))
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    if request.method == "POST":
        start  = request.POST['start']
        end = request.POST['end']
        incomes = Income.objects.filter(dated__range = [start, end])
        expenses = Expense.objects.filter(date_of_expense__range = [start, end])
        total_income = Income.objects.filter(dated__range =[start, end]).aggregate(Sum('amount'))
        total_expense = Expense.objects.filter(date_of_expense__range =[start, end]).aggregate(Sum('amount'))
        profit = (total_income['amount__sum'] - total_expense['amount__sum'])
        return render(request, "reports/profit_loss.html", 
                {
                'start': start,
                'end': end,
                'incomes': incomes, 
                'expenses':expenses, 
                'total_income': total_income['amount__sum'], 
                'total_expense': total_expense['amount__sum'], 
                'profit': profit,
                'employee': employee, 
                }
            )
    return render(request, "reports/profit_loss.html",
                    {
                        'start':'select Date',
                        'end':'select Date',
                        'incomes':[], 
                        'expenses':[], 
                        'total_income': 0,
                        'total_expense': 0, 
                        'profit': 0, 
                        'employee': employee, 
                        }
                    )

"""
KRA Reports
"""
def kra_report(request):
    if not request.session.get('username'):
        messages.info(request, "Please login again to continue.")
        return HttpResponseRedirect(reverse("accounts:login"))
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    if request.method == "POST":
        start  = request.POST['start']
        end = request.POST['end']
        taxs = Deduction.objects.filter(dated__range = [start, end])
        total_tax = Deduction.objects.filter(dated__range =[start, end]).aggregate(Sum('paye'))
        print(taxs)
        return render(request, "reports/kra_report.html", {
                            'taxs': taxs, 
                            'start': start,
                            'end': end, 
                            'employee': employee, 
                            "total_tax": total_tax['paye__sum'],
                             }
                    )
    return render(request, "reports/kra_report.html", {
                            'employee': employee, 
                            'taxs': [],  
                            "total_tax": 0,
                            'start':'select Date',
                            'end':'select Date',
                            }
                    )
