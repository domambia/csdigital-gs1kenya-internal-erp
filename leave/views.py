from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (DetailView, ListView,
                                  TemplateView, CreateView,
                                  UpdateView, DeleteView)

from django.urls import reverse_lazy
from leave.models import Leave, ApplyLeave
from django.conf import settings

from django.core.mail import send_mail


class LeaveListView(ListView):
    context_object_name = "leaves"
    model = Leave

class LeaveDetailView(DetailView):
    context_object_name = 'leave'
    model = Leave


class LeaveCreateView(CreateView):
    fields = ('name', 'description', 'period')
    model = Leave

class LeaveUpdateView(UpdateView):
    fields = ('name', 'description', 'period')
    model = Leave

class LeaveDeleteView(DeleteView):
    model = Leave
    success_url = reverse_lazy("leave:leave_list")


class CreateApplyLeaveView(CreateView):
    fields = ('start_date', 'end_date', 'employee', 'leave')
    model = ApplyLeave
    template_name = "leave/applyleave_form.html"

class ApplyLeaveListView(ListView):
    context_object_name = "applied_leaves"
    model = ApplyLeave
    template_name = "leave/applyleave_list.html"




"""
Leave Operations

"""

# approve the leave
def approve_leave(request, pk):

    leave = ApplyLeave.objects.get(id = pk)
    if(leave):
        leave.status = 1
        leave.save()
        '''
            Send Email
        '''
        from_email="hr@gs1kenya.org"
        to_email = leave.employee.user.email
        subject="Approved Leave and Effective as From Tomorrow"
        content ="""
            Dear {} {},

            Your leave has been approved Today its will be starting as form {} to {}.
            Please hand on the necessary documents to your department Effectively and Immediately.

            Thank you.
            HR. GS1Kenya
            """
        send = send_mail(subject, content.format(leave.employee.user.first_name,
                        leave.employee.user.first_name, leave.start_date, leave.end_date), from_email, [to_email])
        if(send):
            print("Send Email")
        else:
            print("Omambia Email not sent")

        return HttpResponseRedirect(reverse('leave:applyleave_list'))
    print("Not Updated Today")
    return HttpResponseRedirect(reverse('leave:applyleave_list'))
