from django.shortcuts import render, get_object_or_404
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
from CRM.forms import TrainForm, EditClient
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
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

class ClientCreateView(SuccessMessageMixin, CreateView):
    fields = ('company_name', 'company_phone', 'company_phone_alt', 'company_email','certificate_of_incorporation','copy_of_id', 'copy_of_blank_cheque',
            'copy_of_trade_licence', 'list_of_product_barcoded', 'director_pin_number', 'company_certificate_pin', 'copy_of_kebs_certicate',
             'company_email_alt', 'post_address', 'physical_location', 'director_info','sector','date_of_issue', 'nature_of_business')
    model = Client
    success_message = "Successfully! Created a member"
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

class ClientUpdateView(SuccessMessageMixin,UpdateView):
    model = Client
    fields = ('company_name', 'company_phone', 'company_phone_alt', 'company_email','certificate_of_incorporation','copy_of_id', 'copy_of_blank_cheque',
            'copy_of_trade_licence', 'list_of_product_barcoded', 'director_pin_number', 'company_certificate_pin', 'copy_of_kebs_certicate',
             'company_email_alt', 'post_address', 'physical_location', 'director_info','sector','date_of_issue', 'nature_of_business')
    success_message = "Sucessfully! Updated member details"
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
    messages.success(request, "Member Executive. Successfully! Approved member")
    print("ME1 -Approved")
    notify(employee.phone , employee.user.first_name, employee.user.last_name, client.company_name, datetime.now().date())
    return HttpResponseRedirect(reverse('CRM:list_client'))
    # Membership two
def membership_2(request, pk):
    client = Client.objects.get(id = pk)
    client.is_me2 = 1
    client.save()
    messages.success(request, "Member Executive. Successfully! Approved member")
    print("ME2 -Approved")
    return HttpResponseRedirect(reverse('CRM:list_client'))

def communication(request, pk):
    employee = Employee.objects.get(position = Position.objects.get(initials = "ACCM"))
    client = Client.objects.get(id = pk)
    message  = "Dear {} {},You have been requested to generate profoma invoice for [ {} ],GS1 Kenya,({})"
    msg = message.format(employee.user.first_name, employee.user.last_name, client.company_name, datetime.now())
    client.is_ccm = 1
    client.save()
    print("CCM -Approved")
    SMS().send(employee.phone, msg)
    messages.success(request, "Corporate Communication. Successfully! Approved member")
    return HttpResponseRedirect(reverse('CRM:list_client'))

def accounts_manager(request, pk):
    employee = Employee.objects.get(position = Position.objects.get(initials = "TM"))
    client = Client.objects.get(id = pk)
    client.is_accm = 1
    client.save()
    messages.success(request, "Accounts Manager. Successfully! Approved member")
    print("ACCM -Approved")
    print("ME1 -Approved")
    notify(employee.phone , employee.user.first_name, employee.user.last_name, client.company_name, datetime.now().date())
    return HttpResponseRedirect(reverse('CRM:list_client'))

def accounts(request, pk):
    employee = Employee.objects.get(position = Position.objects.get(initials = "GM"))
    client = Client.objects.get(id = pk)
    client.is_cacc = 1
    client.save()
    print("CACC -Approved")
    notify(employee.phone , employee.user.first_name, employee.user.last_name, client.company_name, datetime.now().date())
    messages.success(request, "Accounts Executive. Successfully! Approved member")
    return HttpResponseRedirect(reverse('CRM:list_client'))

def accounts_ex(request, pk):
    employee = Employee.objects.get(position = Position.objects.get(initials = "TM"))
    client = Client.objects.get(id = pk)
    client.is_cacc_x = 1
    client.save()
    print("CACC_ex -Approved")
    notify(employee.phone , employee.user.first_name, employee.user.last_name, client.company_name, datetime.now().date())
    return HttpResponseRedirect(reverse('CRM:list_client'))

'''
Assign Member Number:
'''
class AssignMemberNumber(UpdateView):
    model = Client
    fields = ('member_number','member_prefix')
    template_name = "client/member_form.html"
    def get_context_data(self, **kwargs):
        context = super(AssignMemberNumber, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context
#choose category for the member
class AddCategoryNumber(UpdateView):
    model = Client
    fields = ('category',)
    template_name = "client/category_form.html"
    def get_context_data(self, **kwargs):
        context = super(AddCategoryNumber, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context



def assign_member_details(request, pk):
    form = EditClient(request.POST or None,
                    instance = get_object_or_404(Client, pk=pk))
    client = Client.objects.get(id = pk)
    phone = client.company_phone
    company_name = client.company_name
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    if request.method == "POST":
        if form.is_valid():
            member_number = form.cleaned_data['member_number']
            member_prefix = form.cleaned_data['member_prefix']
            message = "Dear {} you have been assigned {} as member and {} as prefix number.GS1 KENYA"
            form.save()
            SMS().send(phone, message.format(company_name, member_number, member_prefix))
            return HttpResponseRedirect(reverse('CRM:list_client'))
    return render(request, 'client/member_form.html', {'form': form,
                                            'employee': employee})


def technical(request, pk):
    employee = Employee.objects.get(position = Position.objects.get(initials = "CACC"))
    employee_2 = Employee.objects.get(position = Position.objects.get(initials = "ME1"))
    client = Client.objects.get(id = pk)
    message  = "Dear {} {},You have been requested to generate barcodes for [ {} ],GS1 Kenya,({})"
    msg = message.format(employee.user.first_name, employee.user.last_name, client.company_name, datetime.now())
    message_1  = "Dear {} {},You have been requested to generate reciepts & invoice for [ {} ],GS1 Kenya,({})"
    msg_1 = message.format(employee_2.user.first_name, employee_2.user.last_name, client.company_name, datetime.now())
    tm = client.is_tm = 1
    if tm:
        client.save()
        SMS().send(employee.phone, msg_1)
        SMS().send(employee_2.phone, msg)
        print("TM -Approved")
        messages.success(request, "Technical Executive. Successfully! Approved member")
        return HttpResponseRedirect(reverse('CRM:list_client'))

def general_manager(request, pk):
    client = Client.objects.get(id = pk)
    client.is_gm = 1
    client.status = 1
    client.save()
    message = "Dear {} your membership has been approved with member number  [{}] by GS1 KENYA"
    SMS().send(client.company_phone, message.format(client.company_name, client.member_number))
    messages.success(request, "General Manager. Successfully! Approved member")
    print("GM -Approved")
    return HttpResponseRedirect(reverse('CRM:list_client'))

'''
End of Approval
'''
class ClientDeleteView(SuccessMessageMixin, DeleteView):
    model = Client
    template_name = "client/client_delete_confirm.html"
    success_message = "Successfully! Deleted a member"
    success_url = reverse_lazy("CRM:list_client")
    def get_context_data(self, **kwargs):
        context = super(ClientDeleteView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get( user= user)
        return context

'''
The supplier views

'''
class SupplierCreateView(SuccessMessageMixin, CreateView):
    model = Supplier
    success_message = "Successfully! add a supplier"
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

class SupplierUpdateView(SuccessMessageMixin, UpdateView):
    model = Supplier
    success_message = "Successfully! Updated a supplier"
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

class SupplierDeleteView(SuccessMessageMixin, DeleteView):
    model = Supplier
    success_message = "Successfully! Deleted a supplier"
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

class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    success_message = "Successfully! add a feedback."
    fields = ('client_name', 'feedback', 'status')
    template_name  = "feedback/feedback_form.html"
    def get_context_data(self, **kwargs):
        context = super(FeedbackCreateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context



class FeedbackUpdateView(SuccessMessageMixin, UpdateView):
    model = Feedback
    success_message = "Successfully! Updated a feedback"
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


class FeedbackDeleteView(SuccessMessageMixin, DeleteView):
    model = Feedback
    success_message  = "Successfully! Deleted a feedback"
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

class TrainingCreateView(SuccessMessageMixin, CreateView):
    model = Training
    success_message = "Successfully! Created a training"
    fields = ('trainer', 'happened_on', 'all_trainee', 'description')
    template_name  = "training/training_form.html"
    def get_context_data(self, **kwargs):
        context = super(TrainingCreateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user=user)
        return context

class TrainingUpdateView(SuccessMessageMixin, UpdateView):
    model = Training
    success_message = "Successfully! Updated a training .."
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


class TrainingDeleteView(SuccessMessageMixin, DeleteView):
    model = Training
    success_message = "Successfully! Deleted a training"
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
class CreateEventView(SuccessMessageMixin, CreateView):
    model = Event
    success_message  = "Successfully! Created a training event"
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

class UpdateEventView(SuccessMessageMixin, UpdateView):
    model = Event
    success_message = "Successfully! Updated training event"
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

class DeleteEventView(SuccessMessageMixin, DeleteView):
    model = Event
    success_message  = "Successfully! Deleted a training event"
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

class BarcodeCreateView(SuccessMessageMixin, CreateView):
    fields = ('GTIN', 'client', 'product_description', 'brand_name', 'name_packaging', 'type',
                'depth', 'width', 'height', 'gross_weight', 'net_weight', 'size')
    model = Barcode
    success_message = "Successfully! Create a barcode and assigned it t a member"
    template_name  = "barcode/barcode_form.html"
    def get_context_data(self, **kwargs):
        context = super(BarcodeCreateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user)
        return context

class BarcodeUpdateView(SuccessMessageMixin, UpdateView):
    fields = ('GTIN', 'client', 'product_description', 'brand_name', 'name_packaging', 'type',
                'depth', 'width', 'height', 'gross_weight', 'net_weight', 'size')
    model = Barcode
    success_message = "Successfully! Updated a barcode bank for a member"
    template_name  = "barcode/barcode_form.html"
    def get_context_data(self, **kwargs):
        context = super(BarcodeUpdateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['employee'] = Employee.objects.get(user = user)
        return context


class BarcodeDeleteView(SuccessMessageMixin, DeleteView):
    model = Barcode
    success_message = "Sucessfully! Deleted a barcode for a member"
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
