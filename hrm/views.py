from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from accounts.models import Employee
# Create your views here.

class IndexView(ListView):
    context_object_name = 'users'
    model = Employee
    template_name = "hrm/dashboard.html"
