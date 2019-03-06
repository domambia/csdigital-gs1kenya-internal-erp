from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from accounts.models import Employee
from leave.models import ApplyLeave 
from departments.models import Department, Position 
from django.contrib.auth.models import User
from hrm.models import Performance 
from django.urls import reverse_lazy
from hrm.forms import PerformanceForm
# Create your views here.

def index(request):
    applied_leaves = ApplyLeave.objects.count()
    employees = Employee.objects.count()
    positions = Position.objects.count()
    departments = Department.objects.count()
    user = User.objects.get(username = request.session['username'])
    employee = Employee.objects.get(user = user.id)

    return render(request, "hrm/dashboard.html", 
                    {'employees': employees, 'positions': positions, 'departments': departments,
                     'applied_leaves': applied_leaves, "employee": employee, "user":user})


'''
Perfomance Control 
'''

class CreatePerformanceView(CreateView):
    model = Performance 
    fields = ('employee', 'start_date', 'finish_date', 'objective')

    template_name = "hrm/perfomance/performance_form.html"
    def get_context_data(self, **kwargs):
        context = super(CreatePerformanceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context 


class ListPerformanceView(ListView):
    model = Performance 
    context_object_name = "performances"
    template_name = "hrm/perfomance/performance_list.html"
    def get_context_data(self, **kwargs):
        context = super(ListPerformanceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context 


class UpdatePerformanceView(UpdateView):
    model = Performance 
    fields = ('employee', 'start_date', 'finish_date', 'objective')
    template_name = "hrm/perfomance/performance_form.html"
    def get_context_data(self, **kwargs):
        context = super(UpdatePerformanceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context 


class DetailPerformanceView(DetailView):
    model = Performance 
    context_object_name = "perfomance"
    template_name = "hrm/perfomance/performance_form.html"
    def get_context_data(self, **kwargs):
        context = super(DetailPerformanceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context 


class DeleltePerformanceView(DeleteView):
    model = Performance 
    success_url = reverse_lazy("hrm:perform_ist")
    template_name = "hrm/perfomance/performance_delete.html"
    def get_context_data(self, **kwargs):
        context = super(CreatePerformanceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context 

'''
Showing an employees perfomance control
'''
def show_employee_perfomance_control(request):
    employee = Employee.objects.get(user= User.objects.get(username = request.session['username']).id)
    perform = Performance.objects.get(employee = employee.id)

    return render(request, "hrm/performance/employee_performance.html", {'employee': employee, 'perform': perform})



'''
Employee Provide Notes for his perfomance
'''
def perfomance_notes(request, pk):
    form = PerformanceForm(request.POST or None,instance = get_object_or_404(Performance, pk=pk))
    perfom = Performance.objects.get(id =pk)
    employee = Employee.objects.get(user= User.objects.get(username = request.session['username']).id)
    if form.is_valid():
        form.save()
        perfom.status = 1
        perfom.save()
        return "show your perform list"
    return render(request, "hrm/performance/notes.html")

