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
from easy_pdf.views import PDFTemplateResponseMixin


class LeaveListView(ListView):
    context_object_name = "leaves"
    model = Leave

class LeaveDetailView(DetailView):
    context_object_name = 'leave'
    model = Leave


class LeaveCreateView(CreateView):
    fields = ('name', 'description',)
    model = Leave

class LeaveUpdateView(UpdateView):
    fields = ('name', 'description',)
    model = Leave

class LeaveDeleteView(DeleteView):
    model = Leave
    success_url = reverse_lazy("leave:leave_list")


# class CreateApplyLeaveView(CreateView):
#     fields = (
#             'start_date', 'resume_date', 'home_phone','person_taking_charge', 'leave', 'employee',
#             'end_date', 'period'
#         )
#     model = ApplyLeave
#     template_name = "leave/applyleave_form.html"

def applyleave(request):
    form = ApplyForm(request.POST or None)
    user_name  = request.session['username']
    user = User.objects.get(username = user_name)
    emp = Employee.objects.get(id = user.id)
    phone_number = emp.alt_phone_number
    # print(employee_user)
    if form.is_valid():
        user_data = form.save()
        return HttpResponseRedirect(reverse('leave:applyleave_list'))
    

    return render(request,"leave/applyleave_form.html", {'current_user': user_name, 'phone_number': phone_number, 'form': form})
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

        return HttpResponseRedirect(reverse('leave:applyleave_list'))
    print("Not Updated Today")
    return HttpResponseRedirect(reverse('leave:applyleave_list'))

'''
Create pdf 
'''
def create_pdf(request):
    return ""
'''
View to Download a user leave 
'''

def leave_download(request, pk): 
    leave = ApplyLeave.objects.get(pk=pk)
    start_date = leave.start_date 
    end_date = leave.end_date 
    resume_date = leave.resume_date 
    home_phone = leave.home_phone
    leave_name = leave.leave.name 
    
    return "SOme text"


class CreatePDF(PDFTemplateResponseMixin, DetailView):
    model = ApplyLeave
    context_object_name = "leave"
    template_name = "leave/leave_pdf.html"
    
