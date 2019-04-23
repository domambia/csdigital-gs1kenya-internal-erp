from ACCNTS.models import Asset, Income, Liability, Bank
from  django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import Employee
from django.urls import reverse_lazy

class AssetCreateView(CreateView):
    model = Asset
    fields = ('name', 'type', 'memo', 'amount')
    template_name  = "asset/asset_form.html"
    success_message = "Successfully! Create an asset"
    def get_context_data(self, **kwargs):
        context = super(AssetCreateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class AssetUpdateView(UpdateView):
    model = Asset
    fields = ('name', 'type', 'memo', 'amount')
    template_name  = "asset/asset_form.html"
    success_message = "Successfully! Update an asset"
    def get_context_data(self, **kwargs):
        context = super(AssetUpdateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class AssetListView(ListView):
    model = Asset
    template_name  = "asset/asset_list.html"
    context_object_name  = "assets"

    def get_context_data(self, **kwargs):
        context = super(AssetListView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class AssetDetailView(DetailView):
    model = Asset
    context_object_name = 'asset'
    template_name  = "asset/asset_detail.html"

    def get_context_data(self, **kwargs):
        context = super(AssetDetailView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class AssetDeleteView(DeleteView):
    model = Asset
    template_name  = "asset/asset_delete.html"
    success_message = "Successfully! deleted an asset"
    success_url = reverse_lazy("ACCNTS:asset_list")
    def get_context_data(self, **kwargs):
        context = super(AssetDeleteView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context

'''
The Views for Liabilities
'''


class LiabilityCreateView(CreateView):
    model = Liability
    fields = ('name', 'type', 'memo', 'amount')
    template_name  = "liability/liability_form.html"
    success_message = "Successfully! Create a Liability"
    def get_context_data(self, **kwargs):
        context = super(LiabilityCreateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class LiabilityUpdateView(UpdateView):
    model = Liability
    fields = ('name', 'type', 'memo', 'amount')
    template_name  = "liability/liability_form.html"
    success_message = "Successfully! Update an Liability"
    def get_context_data(self, **kwargs):
        context = super(LiabilityUpdateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class LiabilityListView(ListView):
    model = Liability
    template_name  = "liability/liability_list.html"
    context_object_name  = "liabilitys"
    def get_context_data(self, **kwargs):
        context = super(LiabilityListView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class LiabilityDetailView(DetailView):
    model = Liability
    context_object_name = 'liability'
    template_name  = "liability/liability_detail.html"
    def get_context_data(self, **kwargs):
        context = super(LiabilityDetailView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class LiabilityDeleteView(DeleteView):
    model = Liability
    template_name  = "liability/liability_delete.html"
    success_message = "Successfully! deleted a liability"
    success_url = reverse_lazy("ACCNTS:liability_list")
    def get_context_data(self, **kwargs):
        context = super(AssetDeleteView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context

'''
The views for Income
'''

class IncomeCreateView(CreateView):
    model = Income
    fields = ('member', 'type', 'name','memo', 'amount')
    template_name  = "income/income_form.html"
    success_message = "Successfully! Create an income"
    def get_context_data(self, **kwargs):
        context = super(IncomeCreateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class IncomeUpdateView(UpdateView):
    model = Income
    fields = ('member', 'type', 'memo', 'name', 'amount')
    template_name  = "income/income_form.html"
    success_message = "Successfully! Update an income"
    def get_context_data(self, **kwargs):
        context = super(IncomeUpdateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class IncomeListView(ListView):
    model = Income
    template_name  = "income/income_list.html"
    context_object_name  = "incomes"

    def get_context_data(self, **kwargs):
        context = super(IncomeListView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class IncomeDetailView(DetailView):
    model = Income
    context_object_name = 'income'
    template_name  = "income/income_detail.html"

    def get_context_data(self, **kwargs):
        context = super(IncomeDetailView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class IncomeDeleteView(DeleteView):
    model = Income
    template_name  = "income/income_delete.html"
    success_message = "Successfully! deleted an income"
    success_url = reverse_lazy("ACCNTS:income_list")
    def get_context_data(self, **kwargs):
        context = super(IncomeDeleteView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


'''
The Banking Views'''

class BankCreateView(CreateView):
    model = Bank
    fields = ('type', 'ref_number','name', 'banked', 'amount',)
    template_name  = "bank/bank_form.html"
    success_message = "Successfully! Create a bank item"
    def get_context_data(self, **kwargs):
        context = super(BankCreateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class BankListView(ListView):
    model = Bank
    template_name  = "bank/bank_list.html"
    context_object_name = 'banks'
    def get_context_data(self, **kwargs):
        context = super(BankListView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context


class BankUpdateView(UpdateView):
    model = Bank
    fields = ('type', 'ref_number', 'name', 'banked', 'amount',)
    template_name  = "bank/bank_form.html"
    success_message = "Successfully! Updated a bank item"
    def get_context_data(self, **kwargs):
        context = super(BankUpdateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context

class BankDetailView(DetailView):
    model = Bank
    template_name  = "bank/bank_detail.html"
    context_object_name = 'bank'
    def get_context_data(self, **kwargs):
        context = super(BankDetailView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context

class BankDeleteView(DeleteView):
    model = Bank
    template_name  = "bank/bank_delete.html"
    success_message = "Successfully! Deleted a bank item"
    success_url = reverse_lazy("")
    def get_context_data(self, **kwargs):
        context = super(BankCreateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = User.objects.get(username = self.request.user).id)
        return context
