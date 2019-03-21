from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from ACCNTS.models import Expense
from django.urls import reverse_lazy
from accounts.models import Employee
from django.contrib.auth.models import User

'''
Adding an Expense
'''
class CreateExpenseView(SuccessMessageMixin, CreateView):
    model = Expense
    fields = ('vendor', 'date_of_expense', 'amount', 'memo', 'terms_of_payment',
              'VAT', 'ref_no', 'expense_type', 'bill_due', 'payment_method')
    success_message = "Successfully! Created an Purchase/Expense"
    template_name = "expenses/expense_form.html"
    def get_context_data(self, **kwargs):
        context  = super(CreateExpenseView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user  = User.objects.get(username = self.request.user).id)
        return context

'''
Updating Specific Expense
'''
class UpdateExpenseView(SuccessMessageMixin, UpdateView):
    model = Expense
    fields = ('vendor', 'date_of_expense', 'amount', 'memo', 'terms_of_payment',
              'VAT', 'ref_no', 'expense_type', 'bill_due', 'payment_method')
    success_message = "Successfully! Updated an Expense / Purchase"
    template_name = "expenses/expense_form.html"
    def get_context_data(self, **kwargs):
        context  = super(UpdateExpenseView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user  = User.objects.get(username = self.request.user).id)
        return context


'''
List all  Expenses
'''
class ListExpenseView(SuccessMessageMixin, ListView):
    model = Expense
    context_object_name  = "expenses"
    template_name = "expenses/expense_list.html"
    def get_context_data(self, **kwargs):
        context  = super(ListExpenseView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user  = User.objects.get(username = self.request.user).id)
        return context

'''
Adding a sale for  a specific invoice
'''
class DeleteExpenseView(SuccessMessageMixin, DeleteView):
    model = Expense
    success_message = "Successfully! Deleted an Expense / Purchase"
    template_name = "expenses/expense_delete.html"
    success_url = reverse_lazy("ACCNTS:expense_list")
    def get_context_data(self, **kwargs):
        context  = super(DeleteExpenseView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user  = User.objects.get(username = self.request.user).id)
        return context

'''
Get Specific expense
'''
class DetailExpenseView(SuccessMessageMixin, DetailView):
    model = Expense
    context_object_name  = 'expense'
    template_name = "expenses/expense_detail.html"
    def get_context_data(self, **kwargs):
        context  = super(DetailExpenseView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user  = User.objects.get(username = self.request.user).id)
        return context

