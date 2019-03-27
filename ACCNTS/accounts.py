from ACCNTS.models import Asset, Income, Liability
from  django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import Employee



class AssetCreateView(CreateView):
    model = Asset
    fields = ('name', 'type', 'memo', 'amount')
    template_name  = "accounts/asset/asset_form.html"
    success_message = "Successfully! Create an asset"
    def get_context_data(self, **kwargs):
        context = super(AssetCreateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context


class AssetUpdateView(UpdateView):
    model = Asset
    fields = ('name', 'type', 'memo', 'amount')
    template_name  = "accounts/asset/asset_form.html"
    success_message = "Successfully! Update an asset"
    def get_context_data(self, **kwargs):
        context = super(AssetUpdateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context


class AssetListView(ListView):
    model = Asset
    template_name  = "accounts/asset/asset_list.html"
    context_object_name  = "assets"

    def get_context_data(self, **kwargs):
        context = super(AssetListView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context


class AssetDetailView(DetailView):
    model = Asset
    context_object_name = 'asset'
    template_name  = "accounts/asset/asset_detail.html"

    def get_context_data(self, **kwargs):
        context = super(AssetDetailView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context


class AssetDeleteView(DeleteView):
    model = Asset
    template_name  = "accounts/asset/asset_delete.html"
    success_message = "Successfully! deleted an asset"
    def get_context_data(self, **kwargs):
        context = super(AssetDeleteView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context





'''
The Views for Liabilities
'''


class LiabilityCreateView(CreateView):
    model = Liability
    fields = ('name', 'type', 'memo', 'amount')
    template_name  = "accounts/laibility/laibility_form.html"
    success_message = "Successfully! Create a Liability"
    def get_context_data(self, **kwargs):
        context = super(LiabilityCreateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context


class LiabilityUpdateView(UpdateView):
    model = Liability
    fields = ('name', 'type', 'memo', 'amount')
    template_name  = "accounts/liability/liability_form.html"
    success_message = "Successfully! Update an Liability"
    def get_context_data(self, **kwargs):
        context = super(LiabilityUpdateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context


class LiabilityListView(ListView):
    model = Liability
    template_name  = "accounts/laibility/liability_list.html"
    context_object_name  = "liabilities"
    def get_context_data(self, **kwargs):
        context = super(LiabilityListView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context


class LiabilityDetailView(DetailView):
    model = Liability
    context_object_name = 'laibility'
    template_name  = "accounts/liability/asset_detail.html"
    def get_context_data(self, **kwargs):
        context = super(LiabilityDetailView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context


class LiabilityDeleteView(DeleteView):
    model = Liability
    template_name  = "accounts/liability/liability_delete.html"
    success_message = "Successfully! deleted a liability"
    def get_context_data(self, **kwargs):
        context = super(AssetDeleteView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context

'''
The views for Income
'''

class IncomeCreateView(CreateView):
    model = Income
    fields = ('name', 'type', 'memo', 'amount')
    template_name  = "accounts/income/income_form.html"
    success_message = "Successfully! Create an income"
    def get_context_data(self, **kwargs):
        context = super(IncomeCreateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context


class IncomeUpdateView(UpdateView):
    model = Income
    fields = ('name', 'type', 'memo', 'amount')
    template_name  = "accounts/income/income_form.html"
    success_message = "Successfully! Update an income"
    def get_context_data(self, **kwargs):
        context = super(IncomeUpdateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context


class IncomeListView(ListView):
    model = Income
    template_name  = "accounts/income/income_list.html"
    context_object_name  = "incomes"

    def get_context_data(self, **kwargs):
        context = super(IncomeListView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context


class IncomeDetailView(DetailView):
    model = Income
    context_object_name = 'income'
    template_name  = "accounts/income/income_detail.html"

    def get_context_data(self, **kwargs):
        context = super(IncomeDetailView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context


class IncomeDeleteView(DeleteView):
    model = Income
    template_name  = "accounts/income/income_delete.html"
    success_message = "Successfully! deleted an income"
    def get_context_data(self, **kwargs):
        context = super(IncomeDeleteView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(user = self.request.user).id)
        return context



