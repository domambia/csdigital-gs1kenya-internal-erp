from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (DetailView, ListView,
                                  TemplateView, CreateView,
                                  UpdateView, DeleteView)
from leave.forms import ApplyForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from accounts.models import Employee
from leave.models import Leave, ApplyLeave
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from easy_pdf.rendering import render_to_pdf_response
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from helpers.utils import render_to_pdf
from helpers.help import check_user_login

class LeaveListView(ListView):
    context_object_name = "leaves"
    model = Leave
    def get_context_data(self, **kwargs):
        context = super(LeaveListView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context


class LeaveDetailView(DetailView):
    context_object_name = 'leave'
    model = Leave
    def get_context_data(self, **kwargs):
        context = super(LeaveDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context


class LeaveCreateView(SuccessMessageMixin, CreateView):
    fields = ('name', 'description',)
    model = Leave
    success_message = "Successfully! Created type of a leave"
    context_object_name = "form"
    def get_context_data(self, **kwargs):
        context = super(LeaveCreateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context

class LeaveUpdateView(SuccessMessageMixin, UpdateView):
    fields = ('name', 'description',)
    model = Leave
    success_message = "Successfully! Update a leave type"
    context_object_name = "form"
    def get_context_data(self, **kwargs):
        context = super(LeaveUpdateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context

class LeaveDeleteView(SuccessMessageMixin, DeleteView):
    model = Leave
    success_message = "Successfully! Deleted a leave type"
    success_url = reverse_lazy("leave:leave_list")
    def get_context_data(self, **kwargs):
        context = super(LeaveDeleteView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context


class CreateApplyLeaveView(SuccessMessageMixin, CreateView):
    model = ApplyLeave
    fields = ('start_date', 'resume_date', 'home_phone','person_taking_charge', 'leave', 'employee', 'end_date')
    context_object_name = 'form'
    success_message = "Sucessfully! Applied for a leave"
    template_name = "leave/applyleave_form.html"
    def get_context_data(self, **kwargs):
        context = super(CreateApplyLeaveView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        context['current_user'] = User.objects.get(username = self.request.user)
        context['phone_number'] = context['employee'].alt_phone_number
        print(context)
        return context
def list_applyleave(request):
    check_user_login(request)
    leaves = ApplyLeave.objects.all()
    current_user = User.objects.get(username = request.session['username'])
    user_leaves = ApplyLeave.objects.filter(employee = request.session['username'])
    employee = Employee.objects.get(user = current_user.id)

    return render(request, "leave/applyleave_list.html", {"leaves": leaves, "employee": employee, "user_leaves": user_leaves})

class ApplyLeaveUpdateView(SuccessMessageMixin, UpdateView):
    model = ApplyLeave
    fields = (
            'start_date', 'resume_date', 'home_phone','person_taking_charge', 'leave', 'employee',
            'end_date'
        )
    success_message = "Successfully! Updated applied leave"
    template_name = "leave/applyleave_form.html"
    def get_context_data(self, **kwargs):
        context = super(ApplyLeaveUpdateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user.id)
        return context


# approve the leave
def approve_leave(request, pk):
    check_user_login(request)
    leave = ApplyLeave.objects.get(id = pk)
    start_date = leave.start_date
    end_date = leave.end_date
    resume_date = leave.resume_date
    home_phone = leave.home_phone
    leave_name = leave.leave.name
    if(leave):
        leave.status = 1
        leave.save()
        '''
            Send Email
        '''
        from_email="hr@gs1kenya.org"
        user = User.objects.get(username = leave.employee)
        to_email = user.email
        subject="Approved Leave and Effective as From Tomorrow"
        content ="""
            Dear {} {},

            Your leave has been approved Today its will be starting as form {} to {}.
            Please hand on the necessary documents to your department Effectively and Immediately.
            Pick the fully signed document from the HR Office by the End of the Day.

            Thank you.
            HR. GS1Kenya
            """
        send = send_mail(subject, content.format(user.first_name,
                        user.first_name, leave.start_date, leave.end_date), from_email, [to_email])
        if(send):
            print("Send Email")
        else:
            print("Omambia Email not sent")
        messages.success(request, "successfully! Approved a leave and sent and email to employee")
        return HttpResponseRedirect(reverse('leave:applyleave_list'))
    print("Not Updated Today")
    messages.error("Leave not approved. Contact the administrator")
    return HttpResponseRedirect(reverse('leave:applyleave_list'))

'''
Create pdf
'''



def render_pdf_docs(request, pk):
    check_user_login(request)
    leave = ApplyLeave.objects.get(pk=pk)
    user  = User.objects.get(username = leave.employee)
    employee = Employee.objects.get(user = user.id)
    start_date = leave.start_date
    end_date = leave.end_date
    days =  float((end_date - start_date).days)
    return render_to_pdf("leave/leave_pdf.html", {"leave": leave,
                                    "employee": employee, "days": days, "user": user})

