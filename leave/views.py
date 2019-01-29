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
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas



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


class CreateApplyLeaveView(CreateView):
    fields = (
            'start_date', 'resume_date', 'home_phone','person_taking_charge', 'leave', 'employee',
            'end_date', 'period'
        )
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
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    return FileResponse(buffer, as_attachment=True, filename='{}.pdf'.format(leave.employee.user.username+'_leave'))

