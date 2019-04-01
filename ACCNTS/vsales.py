from django.shortcuts import render
from ACCNTS.models import Sales
from accounts.models import Employee
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (CreateView,
                                  UpdateView,
                                  DeleteView,
                                  DetailView,
                                  ListView)
'''
Adding a sale for  a specific invoice
'''
class CreateSalesView(SuccessMessageMixin, CreateView):
    model = Sales
    fields = ('member', 'invoice', 'payment_due', 'payment_terms',)
    success_message = "Successfully! Created a sale"
    template_name = "sales/sales_form.html"
    def get_context_data(self, **kwargs):
        context  = super(CreateSalesView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user  = User.objects.get(username = self.request.user).id)
        return context

'''
Listing all the sales
'''

class ListSalesView(SuccessMessageMixin, ListView):
    model = Sales
    context_object_name  = "sales"
    fields = ('member', 'invoice', 'payment_due', 'payment_terms',)
    template_name = "sales/sales_list.html"
    def get_context_data(self, **kwargs):
        context  = super(ListSalesView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user  = User.objects.get(username = self.request.user).id)
        return context


class UpdateSalesView(SuccessMessageMixin, UpdateView):
    model = Sales
    fields = ('member', 'invoice', 'payment_due', 'payment_terms', 'amount',)
    success_message = "Successfully! Update a sale"
    template_name = "sales/sales_form.html"
    def get_context_data(self, **kwargs):
        context  = super(UpdateSalesView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user  = User.objects.get(username = self.request.user).id)
        return context


class DeleteSalesView(SuccessMessageMixin, DeleteView):
    model = Sales
    success_url = reverse_lazy("ACCNTS:sales_list")
    success_message = "Successfully! Deleted a sale"
    template_name = "sales/sales_delete.html"
    def get_context_data(self, **kwargs):
        context  = super(DeleteSalesView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user  = User.objects.get(username = self.request.user).id)
        return context


class DetailSalesView(SuccessMessageMixin, DetailView):
    model = Sales
    context_object_name  = "sale"
    template_name = "sales/sales_detail.html"
    def get_context_data(self, **kwargs):
        context  = super(DetailSalesView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user  = User.objects.get(username = self.request.user).id)
        return context


