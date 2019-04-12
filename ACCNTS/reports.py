from ACCNTS.models import Sales, Bank, Expense, Liability, Asset, Income
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import datetime
from django.contrib.auth.models import User
from accounts.models import Employee
from django.db.models import Sum
from helpers.help import check_user_login
'''
Sales Report'''

def sales_report(request):
    check_user_login(request)
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    if request.method == "POST":
        start  = request.POST['start']
        end = request.POST['end']
        print("The date is coming.{}".format(start))
        sales = Sales.objects.filter(date_of_sale__range = [start, end])
        type(sales)
        #total = Sales.objects.filter(date_of_sale__range =[start, end]).aggregate(Sum('amount'))
        #print(total)
        return render(request, "sales/sales_report.html", {'sales': sales, 'employee': employee })
    return render(request, "sales/sales_report.html", {'employee': employee, 'sales': []})

def expenses_report(request):
    check_user_login(request)
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    if request.method == "POST":
        start  = request.POST['start']
        end = request.POST['end']
        results = Expense.objects.filter(date_of_expense__range = [start, end])
        total = Expense.objects.filter(date_of_expense__range =[start, end]).aggregate(Sum('amount'))
        print("ksh."+ str(total['amount__sum']))
        return render(request, "expenses/expense_report.html", {'results': results, 'employee': employee, "total": total['amount__sum'] })
    return render(request, "expenses/expense_report.html", {'employee': employee, 'results': [],  "total": 0})

