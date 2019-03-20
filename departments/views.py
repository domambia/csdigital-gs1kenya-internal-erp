from django.shortcuts import render
from departments import models
from django.urls import reverse_lazy
from accounts.models import Employee
from django.views.generic import (DetailView,
                                 ListView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView )
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class CreateDepartmentView(SuccessMessageMixin, CreateView):
    fields = ('name', 'initials')
    model = models.Department
    success_message = "Successfully! Created %(name)s department"
    template_name = "departments/department_form.html"
    def get_context_data(self, **kwargs):
        context = super(CreateDepartmentView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context


class ListDepartmentsView(ListView):
    context_object_name = "departments"
    model = models.Department
    template_name = "departments/departments_list.html"
    def get_context_data(self, **kwargs):
        context = super(ListDepartmentsView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context

class DetailDepartmentView(DetailView):
    context_object_name = "department"
    model = models.Department
    def get_context_data(self, **kwargs):
        context = super(DetailDepartmentView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context

class UpdateDepartmentView(SuccessMessageMixin, UpdateView):
    fields = ('name', 'initials')
    model = models.Department
    success_message = "Successfully! Update %(name)s department"
    def get_context_data(self, **kwargs):
        context = super(UpdateDepartmentView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context


class DeleteDepartmentView(SuccessMessageMixin, DeleteView):
    model = models.Department
    success_message = "Successfully! Deleted a department"
    success_url = reverse_lazy("departments:list_department")
    def get_context_data(self, **kwargs):
        context = super(DeleteDepartmentView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context



""" Job Positions in GS1 company
Author: Omambia Mogaka Dauglous
This helps in the manipulation of the Job Positons Part for
the GS1 ERP systemself.
"""

class CreatePositionView(SuccessMessageMixin, CreateView):
    fields = ('name', 'initials', 'department')
    model = models.Position
    context_object_name = "form"
    success_message = "Sucessfully! Created a new job position"
    template_name = "departments/position_form.html"
    def get_context_data(self, **kwargs):
        context = super(CreatePositionView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context

class DetailPositionView(DetailView):
    context_object_name = "position"
    model = models.Position
    template_name = "departments/position_detail.html"
    def get_context_data(self, **kwargs):
        context = super(DetailPositionView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context

class UpdatePositionView(SuccessMessageMixin, UpdateView):
    fields = ('name', 'initials', 'department')
    model = models.Position
    success_message = "Successfully! Update a job position"
    template_name = "departments/position_form.html"
    def get_context_data(self, **kwargs):
        context = super(UpdatePositionView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context

class ListPositionView(ListView):
    context_object_name = "positions"
    model = models.Position
    template_name = "departments/position_list.html"
    def get_context_data(self, **kwargs):
        context = super(ListPositionView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context

class DeletePositionView(SuccessMessageMixin, DeleteView):
    model = models.Position
    success_message = "Successfully! Deleted a Job position"
    success_url = reverse_lazy("departments:list_position")
    def get_context_data(self, **kwargs):
        context = super(DeletePositionView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context
