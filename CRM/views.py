from django.shortcuts import render
from accounts.models import Employee
from django.contrib.auth.models import User
from departments.models import Position
from django.urls import reverse_lazy
from CRM.models import Client, Supplier, Feedback, Training, Barcode, Event
from helpers.help import get_country, get_sectors
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from helpers.sendSMS import SMS
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from helpers.sendSMS import SMS
from CRM.forms import TrainForm
# Create your views here.

'''
The views for the CRM part of the ERP 
The dashboard page
'''

def index(request):
    clients = Client.objects.count()
    suppliers =  Supplier.objects.count()
    feedbacks = Feedback.objects.count()
    trainings = Training.objects.count()
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)

    # sms = SMS()
    # sms.send("+254708067459", "Welcome omambia")
    return render(request, "home/index.html",
                        {'clients': clients, 'suppliers': suppliers, 'feedbacks': feedbacks, 'trainings': trainings, "employee": employee})


'''


'''

class ClientCreateView(CreateView):
    fields = ('company_name', 'company_phone', 'company_phone_alt', 'company_email','certificate_of_incorporation','copy_of_id', 'copy_of_blank_cheque',
            'copy_of_trade_licence', 'list_of_product_barcoded', 'director_pin_number', 'company_certificate_pin', 'copy_of_kebs_certicate',
             'company_email_alt', 'post_address', 'physical_location', 'director_info','sector', 'category', 'date_of_issue', 'nature_of_business')
    model = Client
    template_name = "client/client_form.html"
    def get_context_data(self, **kwargs):
        context = super(ClientCreateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context

# class ClientListView(ListView):
#     model = Client
#     context_object_name = "clients"
#     template_name = "client/client_list.html"

@login_required
def all_clients(request):
    user = User.objects.get(username = request.session['username'])
    employee = Employee.objects.get(user = user.id)
    clients = Client.objects.all()
    return render(request, "client/client_list.html", {"clients": clients, "employee":employee})

class ClientUpdateView(UpdateView):
    model = Client
    fields = ('company_name', 'company_phone', 'company_phone_alt', 'company_email','certificate_of_incorporation','copy_of_id', 'copy_of_blank_cheque',
            'copy_of_trade_licence', 'list_of_product_barcoded', 'director_pin_number', 'company_certificate_pin', 'copy_of_kebs_certicate',
             'company_email_alt', 'post_address', 'physical_location', 'director_info','sector', 'category', 'date_of_issue', 'nature_of_business')
    template_name = "client/client_form.html"
    def get_context_data(self, **kwargs):
        context = super(ClientUpdateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context


class ClientDetailView(DetailView):
    model = Client
    context_object_name = 'client'
    template_name = "client/client_detail.html"
    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context



def clients(request, pk):
    client = Client.objects.get(id = pk)
    user = User.objects.get(username = request.session['username'])
    employee = Employee.objects.get(user = user.id)
    return render(request, "client/client_detail.html", {"client": client, "employee": employee})

'''Approving Clients

'''

def notify(phone, first_name, last_name, company_name, when):
    message  = "Dear {} {},You have been requested to aprove our esteemed member[ {} ].GS1 Kenya,({})"
    msg = message.format(first_name, last_name, company_name, when)
    SMS().send(phone, msg)

def membership(request, pk):
    employee = Employee.objects.get(position = Position.objects.get(initials = "CCM"))
    client = Client.objects.get(id = pk)
    client.is_me1 = 1
    client.save()
    print("ME1 -Approved")
    notify(employee.phone , employee.user.first_name, employee.user.last_name, client.company_name, datetime.now().date())
    return HttpResponseRedirect(reverse('CRM:list_client'))
    # Membership two
def membership_2(request, pk):
    client = Client.objects.get(id = pk)
    client.is_me2 = 1
    client.save()
    print("ME2 -Approved")
    return HttpResponseRedirect(reverse('CRM:list_client'))

def communication(request, pk):
    employee = Employee.objects.get(position = Position.objects.get(initials = "ACCM"))
    client = Client.objects.get(id = pk)
    client.is_ccm = 1
    client.save()
    print("CCM -Approved")
    notify(employee.phone , employee.user.first_name, employee.user.last_name, client.company_name, datetime.now().date())
    return HttpResponseRedirect(reverse('CRM:list_client'))

def accounts_manager(request, pk):
    employee = Employee.objects.get(position = Position.objects.get(initials = "CACC"))
    client = Client.objects.get(id = pk)
    client.is_accm = 1
    client.save()
    print("ACCM -Approved")
    print("ME1 -Approved")
    notify(employee.phone , employee.user.first_name, employee.user.last_name, client.company_name, datetime.now().date())
    return HttpResponseRedirect(reverse('CRM:list_client'))

def accounts(request, pk):
    employee = Employee.objects.get(position = Position.objects.get(initials = "TM"))
    client = Client.objects.get(id = pk)
    client.is_cacc = 1
    client.save()
    print("CACC -Approved")
    notify(employee.phone , employee.user.first_name, employee.user.last_name, client.company_name, datetime.now().date())
    return HttpResponseRedirect(reverse('CRM:list_client'))

'''
Assign Member Number:
'''
class AssignMemberNumber(UpdateView):
    model = Client 
    fields = ('member_number',)
    template_name = "client/member_form.html"
    def get_context_data(self, **kwargs):
        context = super(AssignMemberNumber, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context


def technical(request, pk):
    employee = Employee.objects.get(position = Position.objects.get(initials = "GM"))
    employee_2 = Employee.objects.get(position = Position.objects.get(initials = "ME1"))
    client = Client.objects.get(id = pk)
    message  = "Dear {} {},You have been requested to generate barcodes for [ {} ],GS1 Kenya,({})"
    msg = message.format(employee.user.first_name, employee.user.last_name, client.company_name, datetime.now())
    message_1  = "Dear {} {},You have been requested to generate reciepts & invoice for [ {} ],GS1 Kenya,({})"
    msg_1 = message.format(employee_2.user.first_name, employee_2.user.last_name, client.company_name, datetime.now())
    
    tm = client.is_tm = 1
    if tm:    
        client.save()
        SMS().send(employee.phone, msg)
        SMS().send(employee_2.phone, msg_1)
        print("TM -Approved")
        return HttpResponseRedirect(reverse('CRM:assign', args=(pk,)))

def general_manager(request, pk):
    # employee = Employee.objects.get(position = Position.objects.get(initials = "CCM"))
    client = Client.objects.get(id = pk)
    client.is_gm = 1
    client.status = 1
    client.save()
    # notify(employee.phone , employee.user.first_name, employee.user.last_name, client.company_name, datetime.now)
    print("GM -Approved")
    return HttpResponseRedirect(reverse('CRM:list_client'))


'''
End of Approval
'''
class ClientDeleteView(DeleteView):
    model = Client
    template_name = "client/client_delete_confirm.html"
    success_url = reverse_lazy("CRM:delete_client")



'''
The supplier views

'''
class SupplierCreateView(CreateView):
    model = Supplier
    fields = ('name', 'phone', 'country', 'website', 'description')
    template_name = "supplier/supplier_form.html"
    def get_context_data(self, **kwargs):
        context = super(SupplierCreateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get( user= user)
        return context

class SupplierListView(ListView):
    model = Supplier
    context_object_name = "suppliers"
    template_name = "supplier/supplier_list.html"
    def get_context_data(self, **kwargs):
        context = super(SupplierListView, self).get_context_data(**kwargs)
        user = self.request.user
        print(user)
        context['employee'] = Employee.objects.get(user = user)
        return context

class SupplierUpdateView(UpdateView):
    model = Supplier
    fields = ('name', 'phone', 'country', 'website', 'description')
    template_name = "supplier/supplier_form.html"
    def get_context_data(self, **kwargs):
        context = super(SupplierUpdateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context

class SupplierDetailView(DetailView):
    model = Supplier
    context_object_name = "supplier"
    template_name = "supplier/supplier_detail.html"
    def get_context_data(self, **kwargs):
        context = super(SupplierDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "supplier/supplier_delete_confirm.html"
    success_url = reverse_lazy("CRM:list_supplier")
    def get_context_data(self, **kwargs):
        context = super(SupplierDeleteView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context

'''
The Feedback Views
'''

class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ('client_name', 'feedback', 'status')
    template_name  = "feedback/feedback_form.html"
    def get_context_data(self, **kwargs):
        context = super(FeedbackCreateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context



class FeedbackUpdateView(UpdateView):
    model = Feedback
    fields = ('client_name', 'feedback', 'status')
    template_name  = "feedback/feedback_form.html"
    def get_context_data(self, **kwargs):
        context = super(FeedbackUpdateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context


class FeedbackListView(ListView):
    model = Feedback
    context_object_name  = "feedbacks"
    template_name = "feedback/feedback_list.html"
    def get_context_data(self, **kwargs):
        context = super(FeedbackListView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context


class FeedbackDeleteView(DeleteView):
    model = Feedback
    template_name = "feedback/feedback_delete_confirm.html"
    success_url = reverse_lazy("CRM:list_feedback")
    def get_context_data(self, **kwargs):
        context = super(FeedbackDeleteView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context


class FeedbackDetailView(DetailView):
    model = Feedback
    context_object_name = "feedback"
    template_name = "feedback/feedback_detail.html"
    def get_context_data(self, **kwargs):
        context = super(FeedbackDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context

''' Status ACTIVATIONS '''
@login_required
def unpend(request, pk):
    feedback = Feedback.objects.get(id = pk)
    feedback.status = 11
    feedback.save()
    print(feedback.status)
    return HttpResponseRedirect(reverse('CRM:list_feedback'))

@login_required
def close(request, pk):
    feedback = Feedback.objects.get(id = pk)
    feedback.status = 1
    feedback.save()
    print(feedback.status)
    return HttpResponseRedirect(reverse('CRM:list_feedback'))


'''
The Training Feedback
'''

def get_clients():
    list_clients = Client.objects.all()
    clients = []
    for cl in list_clients:
        clients.append((cl.id, cl.company_name ,))
    return tuple(clients)

class TrainingCreateView(CreateView):
    model = Training 
    fields = ('trainer', 'happened_on', 'all_trainee', 'description')
    template_name  = "training/training_form.html"
    def get_context_data(self, **kwargs):
        context = super(TrainingCreateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context

    
class TrainingUpdateView(UpdateView):
    model = Training
    fields = ('trainer','happened_on', 'all_trainee', 'description')
    template_name  = "training/training_form.html"
    def get_context_data(self, **kwargs):
        context = super(TrainingUpdateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context


class TrainingListView(ListView):
    model = Training
    context_object_name  = "trainings"
    template_name = "training/training_list.html"
    def get_context_data(self, **kwargs):
        context = super(TrainingListView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context


class TrainingDeleteView(DeleteView):
    model = Training
    template_name = "training/training_confirm_delete.html"
    success_url = reverse_lazy("CRM:list_training")
    def get_context_data(self, **kwargs):
        context = super(TrainingDeleteView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context


class TrainingDetailView(DetailView):
    model = Training
    context_object_name = "training"
    template_name = "training/training_detail.html"
    def get_context_data(self, **kwargs):
        context = super(TrainingDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context

'''
Create the Event View
'''
class CreateEventView(CreateView):
    model = Event
    fields = ('event_name', 'training')
    template_name = "event/event_form.html"
    def get_context_data(self, **kwargs):
        context = super(CreateEventView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context


class ListEventView(ListView):
    model = Event
    context_object_name = "events"
    template_name = "event/event_list.html"
    def get_context_data(self, **kwargs):
        context = super(ListEventView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context

class UpdateEventView(UpdateView):
    model = Event
    fields = ('event_name', 'training')
    template_name = "event/event_form.html"
    def get_context_data(self, **kwargs):
        context = super(UpdateEventView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context

class DetailEventView(DetailView):
    model = Event
    content_object_name = "event"
    template_name = "event/event_detail.html"
    def get_context_data(self, **kwargs):
        context = super(DetailEventView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context

class DeleteEventView(DeleteView):
    model = Event
    success_url = "CRM:list_event"
    template_name = "event/event_confirm_delete.html"
    def get_context_data(self, **kwargs):
        context = super(DeleteEventView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context


'''
Barcode Details
'''
class BarcodeListView(ListView):
    model = Barcode
    context_object_name = "barcodes"
    template_name = "barcode/barcode_list.html"
    def get_context_data(self, **kwargs):
        context = super(BarcodeListView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user)
        return context

class BarcodeCreateView(CreateView):
    fields = ('GTIN', 'client', 'product_description', 'brand_name', 'name_packaging', 'type',
                'depth', 'width', 'height', 'gross_weight', 'net_weight', 'size')
    model = Barcode
    template_name  = "barcode/barcode_form.html"
    def get_context_data(self, **kwargs):
        context = super(BarcodeCreateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user)
        return context

class BarcodeUpdateView(UpdateView):
    fields = ('GTIN', 'client', 'product_description', 'brand_name', 'name_packaging', 'type',
                'depth', 'width', 'height', 'gross_weight', 'net_weight', 'size')
    model = Barcode
    template_name  = "barcode/barcode_form.html"
    def get_context_data(self, **kwargs):
        context = super(BarcodeUpdateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user)
        return context


class BarcodeDeleteView(DeleteView):
    model = Barcode
    template_name  = "barcode/barcode_confirm_delete.html"
    success_url = reverse_lazy("CRM:list_barcode")
    def get_context_data(self, **kwargs):
        context = super(BarcodeDeleteView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user)
        return context

class BarcodeDetailView(DetailView):
    model = Barcode
    context_object_name  = 'barcode'
    template_name = "barcode/barcode_detail.html"
    def get_context_data(self, **kwargs):
        context = super(BarcodeDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get( user= user)
        return context

