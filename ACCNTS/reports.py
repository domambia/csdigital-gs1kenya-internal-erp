from ACCNTS.models import Sales, Bank, Expense, Liability, Asset, Income
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
        return render(request, "reports/sales_report.html", {'sales': sales, 'employee': employee })
    return render(request, "reports/sales_report.html", {'employee': employee, 'sales': []})

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
        return render(request, "reports/expense_report.html", {'results': results, 'employee': employee, "total": total['amount__sum'] })
    return render(request, "reports/expense_report.html", {'employee': employee, 'results': [],  "total": 0})

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
        return render(request, "reports/banking_report.html", {'banks': results, 'employee': employee, "total": total['amount__sum'] })
    return render(request, "reports/banking_report.html", {'employee': employee, 'banks': [],  "total": 0})


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
        return render(request, "reports/asset_report.html", {'assets': results, 'employee': employee, "total": total['amount__sum'] })
    return render(request, "reports/asset_report.html", {'employee': employee, 'assets': [],  "total": 0})
