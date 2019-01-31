from django.shortcuts import render
from django.views.generic  import CreateView, ListView, UpdateView, DeleteView, DetailView
from payroll.models import Payroll
from django.urls import reverse_lazy 

# Create your views here.

class PayrollCreateView(CreateView):
    model = Payroll 
    fields  = ('employee', 'payroll_file')
    template_name  = "payroll/payroll_form.html"

class PayrollListView(ListView):
    model = Payroll 
    context_object_name = "payrolls"
    template_name = "payroll/payroll_list.html"

class PayrollUpdateView(UpdateView):
    model = Payroll
    fields  = ('employee', 'payroll_file')
    template_name  = "payroll/payroll_form.html"

class PayrollDetailView(DetailView):
    model = Payroll
    context_object_name = "payroll"
    template_name  = "payroll/payroll_detail.html"

class PayrollDeleteView(DeleteView):
    model = Payroll 
    template_name = "payroll/payroll_confirm_delete.html"
    success_url = reverse_lazy("payroll:list_payroll")

    
# sending to the users
