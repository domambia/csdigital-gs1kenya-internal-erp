from django.shortcuts import render
from .models import Letter, Contract, Category, GS1Docs
from accounts.models import Employee
from django.contrib.auth.models import User
from  helpers.help import check_user_login
def index(request):
    check_user_login(request)

    letters = Letter.objects.count()
    contracts =  Contract.objects.count()
    categorys = Category.objects.count()
    gs1docs = GS1Docs.objects.count()
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)

    return render(request, "dashboard/index.html",
                        {'letters': letters, 'categorys': categorys, 'gs1docs':gs1docs, 'contracts': contracts, "employee": employee})
