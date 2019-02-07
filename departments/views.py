from django.shortcuts import render
from departments import models
from django.urls import reverse_lazy
from django.views.generic import (DetailView,
                                 ListView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView )


class CreateDepartmentView(CreateView):
    fields = ('name', 'initials')
    model = models.Department
    template_name = "departments/department_form.html"


class ListDepartmentsView(ListView):
    context_object_name = "departments"
    model = models.Department
    template_name = "departments/departments_list.html"

class DetailDepartmentView(DetailView):
    context_object_name = "department"
    model = models.Department

class UpdateDepartmentView(UpdateView):
    fields = ('name', 'initials')
    model = models.Department


class DeleteDepartmentView(DeleteView):
    model = models.Department
    success_url = reverse_lazy("departments:list_department")



""" Job Positions in GS1 company
Author: Omambia Mogaka Dauglous
This helps in the manipulation of the Job Positons Part for
the GS1 ERP systemself.
"""

class CreatePositionView(CreateView):
    fields = ('name', 'initials', 'department')
    model = models.Position

    template_name = "departments/position_form.html"

class DetailPositionView(DetailView):
    context_object_name = "position"
    model = models.Position
    template_name = "departments/position_detail.html"

class UpdatePositionView(UpdateView):
    fields = ('name', 'initials', 'department')
    model = models.Position
    template_name = "departments/position_form.html"

class ListPositionView(ListView):
    context_object_name = "positions"
    model = models.Position
    template_name = "departments/position_list.html"

class DeletePositionView(DeleteView):
    model = models.Position
    success_url = reverse_lazy("departments:list_position")
