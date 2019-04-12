from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from helpers.help import check_user_login
# Create your views here.

def index(request):
    check_user_login(request)

    user = request.session['username']
    current_user = User.objects.get(username = user)
    print(current_user.first_name, current_user.last_name )
    return render(request, "homePage/index.html", {'user': current_user})
