from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import Employee
from django.urls import reverse_lazy
from .models import Category, Letter, Contract, GS1Docs
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

'''
Generics Views to help in the GS1Docs Maniputations'''

'''
# GS1Docs Create view'''

class GS1DocsCreateView(CreateView):
    model = GS1Docs

    fields = (
        'name',
        'document',
        'description',
        'status',
    )

    template_name  = "legal/gs1docs/gs1docs_form.html"

    # flash message
    success_message  = "Successfully! Create a gs1 document"

    def get_context_data(self, **kwargs):
        context = super(GS1DocsCreateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context


class GS1DocsUpdateView(UpdateView):
    model = GS1Docs

    fields = (
        'name',
        'document',
        'description',
        'status',
    )
    context_object_name = "gs1doc"
    template_name  = "legal/gs1docs/gs1docs_form.html"

    # flash message
    success_message  = "Successfully! Udpated a gs1 document"

    def get_context_data(self, **kwargs):
        context = super(GS1DocsUpdateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context

    '''List all the gs1Kenya Documents'''
class GS1DocsListView(ListView):
    model = GS1Docs
    #context manager
    context_object_name = "gs1docs"
    template_name  = "legal/gs1docs/gs1docs_list.html"

    def get_context_data(self, **kwargs):
        context = super(GS1DocsListView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context

    '''Getting the gs1Docs'''
class GS1DocsDetailView(DetailView):
    model = GS1Docs
    context_object_name = "gs1doc"
    template_name  = "legal/gs1docs/gs1docs_detail.html"

    def get_context_data(self, **kwargs):
        context = super(GS1DocsDetailView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context

class GS1DocsDeleteView(DeleteView):
    model = GS1Docs
    template_name  = "legal/gs1docs/gs1docs_delete.html"
    success_url = reverse_lazy("Legal:gs1docs_list")
    # flash message
    success_message  = "Successfully! Deleles a gs1 documents"
    def get_context_data(self, **kwargs):
        context = super(GS1DocsDeleteView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context



    '''
The Category Views
    '''

class CategoryCreateView(CreateView):
    model = Category

    fields = (
        'name',
        'description',
        'status',
    )

    template_name  = "legal/category/category_form.html"

    # flash message
    success_message  = "Successfully! Create a category"

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context

class CategoryListView(ListView):
    model = Category
    context_object_name = 'categorys'
    template_name  = "legal/category/category_list.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context

class CategoryDetailView(DetailView):
    model = Category
    context_object_name  = 'category'
    template_name  = "legal/category/category_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context

class CategoryUpdateView(UpdateView):
    model = Category

    fields = (
        'name',
        'description',
        'status',
    )

    template_name  = "legal/category/category_form.html"

    # flash message
    success_message  = "Successfully! Updated a category"

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context

class CategoryDeleteView(DeleteView):
    model = Category
    template_name  = "legal/category/category_delete.html"
    success_url = reverse_lazy("Legal:category_list")
    # flash message
    success_message  = "Successfully! Create a gs1 documents"

    def get_context_data(self, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context


    '''Contract Views'''
class ContractCreateView(CreateView):
    model = Contract

    fields = (
        'name',
        'category',
        'dofsigning',
        'doflapsing',
        'document',
        'description',
        'status',
    )

    template_name  = "legal/contract/contract_form.html"
    # flash message
    success_message  = "Successfully! Create a contract"

    def get_context_data(self, **kwargs):
        context = super(ContractCreateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context


class ContractUpdateView(UpdateView):
    model = Contract
    fields = (
        'name',
        'category',
        'doflapsing',
        'dofsigning',
        'document',
        'description',
        'status',
    )
    template_name  = "legal/contract/contract_form.html"

    # flash message
    success_message  = "Successfully! Udpated a contract"

    def get_context_data(self, **kwargs):
        context = super(ContractUpdateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context


class ContractListView(ListView):
    model = Contract
    context_object_name  = 'contracts'
    template_name  = "legal/contract/contract_list.html"

    def get_context_data(self, **kwargs):
        context = super(ContractListView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context

class ContractDetailView(DetailView):
    model = Contract
    context_object_name  = "contract"
    template_name  = "legal/contract/contract_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ContractDetailView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context

class ContractDeleteView(DeleteView):
    model = Contract
    template_name  = "legal/contract/contract_delete.html"
    success_url = reverse_lazy("Legal:contract_list")
    # flash message
    success_message  = "Successfully! Deleted a contract"
    def get_context_data(self, **kwargs):
        context = super(ContractDeleteView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context



    '''
    Letters Views
    '''

class LetterCreateView(CreateView):
    model = Letter

    fields = (
        'name',
        'document',
        'description',
        'status',
    )

    template_name  = "legal/letter/letter_form.html"
    # flash message
    success_message  = "Successfully! Create a letter"

    def get_context_data(self, **kwargs):
        context = super(LetterCreateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context


class LetterUpdateView(UpdateView):
    model = Letter
    fields = (
        'name',
        'document',
        'description',
        'status',
    )
    template_name  = "legal/letter/letter_form.html"
    # flash message
    success_message  = "Successfully! Udpated a letter"

    def get_context_data(self, **kwargs):
        context = super(LetterUpdateView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context


class LetterListView(ListView):
    model = Letter
    context_object_name  = 'letters'
    template_name  = "legal/letter/letter_list.html"

    def get_context_data(self, **kwargs):
        context = super(LetterListView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        print(context['letters'])
        return context

class LetterDetailView(DetailView):
    model = Letter
    context_object_name  = "letter"
    template_name  = "legal/letter/letter_detail.html"

    def get_context_data(self, **kwargs):
        context = super(LetterDetailView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context

class LetterDeleteView(DeleteView):
    model = Letter
    template_name  = "legal/letter/letter_delete.html"
    success_url = reverse_lazy("Legal:letter_list")
    # flash message
    success_message  = "Successfully! Deleted a letter"
    def get_context_data(self, **kwargs):
        context = super(LetterDeleteView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=User.objects.get(username = self.request.user).id)
        return context
