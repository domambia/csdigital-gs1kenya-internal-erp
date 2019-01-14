from django.shortcuts import render
from targets.models import Target
from django.views.generic import ListView, CreateView, UpdateView,DeleteView, DetailView
from django.urls import reverse_lazy
# Create your views here.

class TargetCreateView(CreateView):
    model = Target 
    fields = ('employee', 'name', 'start_date', 'end_date')

class TargetListView(ListView):
    model = Target
    context_object_name = "targets" 

class TargetUpdateView(UpdateView):
    model = Target 
    fields = ('employee', 'name', 'start_date', 'end_date')

class TargetDeleteView(DeleteView):
    model = Target 
    success_url = reverse_lazy("target:target_list")

class TargetDetailView(DetailView):
    model = Target 
    context_object_name = "target"