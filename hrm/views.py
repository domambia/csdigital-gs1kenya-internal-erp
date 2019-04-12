from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from accounts.models import Employee
from leave.models import ApplyLeave 
from departments.models import Department, Position 
from django.contrib.auth.models import User
from hrm.models import Performance 
from django.urls import reverse_lazy,  reverse
from hrm.forms import PerformanceForm
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from helpers.help import check_user_login
# Create your views here.

def index(request):
    if not request.session.get('username'):
        return HttpResponseRedirect(reverse("accounts:login"))

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

class CreatePerformanceView(SuccessMessageMixin, CreateView):
    model = Performance 
    fields = ('employee', 'start_date', 'finish_date', 'objective')
    success_message  = "Successfully! Created employee and appraisal..."
    template_name = "hrm/performance/performance_form.html"
    def get_context_data(self, **kwargs):
        context = super(CreatePerformanceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context 


class ListPerformanceView(ListView):
    model = Performance 
    context_object_name = "performances"
    template_name = "hrm/performance/performance_list.html"
    def get_context_data(self, **kwargs):
        context = super(ListPerformanceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context 


class UpdatePerformanceView(SuccessMessageMixin, UpdateView):
    model = Performance
    fields = ('employee', 'start_date', 'finish_date', 'objective')
    success_message = "Successfully! Updated an appraisal"
    context_object_name = "performance"
    template_name = "hrm/performance/performance_form.html"
    def get_context_data(self, **kwargs):
        context = super(UpdatePerformanceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context


class DetailPerformanceView(DetailView):
    model = Performance
    context_object_name = "performance"
    template_name = "hrm/performance/performance_details.html"
    def get_context_data(self, **kwargs):
        context = super(DetailPerformanceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context


class DeletePerformanceView(SuccessMessageMixin, DeleteView):
    model = Performance
    success_message = "Successfully! Deleted an appraisal."
    success_url = reverse_lazy("hrm:perfom_list")
    template_name = "hrm/performance/performance_delete.html"
    def get_context_data(self, **kwargs):
        context = super(DeletePerformanceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context

'''
Showing an employees perfomance control
'''
def show_employee_perfomance_control(request):
    check_user_login(request)
    employee = Employee.objects.get(user= User.objects.get(username = request.session['username']).id)
    perform = Performance.objects.filter(employee = employee.id)
    print(perform)
    if perform is None:
        return HttpResponseRedirect(reverse("hrm:hrm_index"))
    return render(request, "hrm/performance/employee_performance.html", {'employee': employee, 'performances': perform})


'''
Employee Provide Notes for his perfomance
'''

def perfomance_notes(request, pk):
    form = PerformanceForm(request.POST or None,instance = get_object_or_404(Performance, pk=pk))
    employee = Employee.objects.get(user= User.objects.get(username = request.session['username']).id)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully! Added notes on what you have done.")
            return HttpResponseRedirect(reverse('hrm:perfom_employee'))
    return render(request, "hrm/performance/performance_notes.html", {'form': form, 'employee': employee})

def appraisal(request, pk):
    perform = Performance.objects.get(id = pk)
    perform.status = 1
    perform.save()
    messages.success(request, "Successfully! Appraised employee work....")
    return HttpResponseRedirect(reverse('hrm:perfom_list'))
