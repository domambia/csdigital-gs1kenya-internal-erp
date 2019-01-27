from django.shortcuts import render
from django.urls import reverse_lazy 
from CRM.models import Client, Supplier, Feedback, Training
from helpers.help import get_country, get_sectors
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView 
# Create your views here.

'''
The dashboard page
'''

def index(request):
    clients = Client.objects.count()
    suppliers =  Supplier.objects.count()
    feedbacks = Feedback.objects.count()
    trainings = Training.objects.count()

    return render(request, "home/index.html", 
                        {'clients': clients, 'suppliers': suppliers, 'feedbacks': feedbacks, 'trainings': trainings})


'''


'''
class ClientCreateView(CreateView):
    fields = ('company_name', 'company_phone', 'company_phone_alt', 'company_email','certificate_of_incorporation','copy_of_id', 'copy_of_blank_cheque',
            'copy_of_trade_licence', 'list_of_product_barcoded', 'director_pin_number', 'company_certificate_pin', 'copy_of_kebs_certicate',
             'company_email_alt', 'post_address', 'physical_location', 'director_info','sector', 'category', 'date_of_issue', 'nature_of_business')
    model = Client 
    template_name = "client/client_form.html"

class ClientListView(ListView):
    model = Client
    context_object_name = "clients"
    template_name = "client/client_list.html"

class ClientUpdateView(UpdateView):
    model = Client
    fields = ('company_name', 'company_phone', 'company_phone_alt', 'company_email','certificate_of_incorporation','copy_of_id', 'copy_of_blank_cheque',
            'copy_of_trade_licence', 'list_of_product_barcoded', 'director_pin_number', 'company_certificate_pin', 'copy_of_kebs_certicate',
             'company_email_alt', 'post_address', 'physical_location', 'director_info','sector', 'category', 'date_of_issue', 'nature_of_business')
    template_name = "client/client_form.html"
class ClientDetailView(DetailView):
    model = Client
    context_object_name = 'client'
    template_name = "client/client_detail.html"

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

class SupplierListView(ListView):
    model = Supplier
    context_object_name = "suppliers"
    template_name = "supplier/supplier_list.html"

class SupplierUpdateView(UpdateView):
    model = Supplier
    fields = ('name', 'phone', 'country', 'website', 'description')
    template_name = "supplier/supplier_form.html"

class SupplierDetailView(DetailView):
    model = Supplier 
    context_object_name = "supplier"
    template_name = "supplier/supplier_detail.html"

class SupplierDeleteView(DeleteView):
    model = Supplier 
    template_name = "supplier/supplier_delete_confirm.html"
    success_url = reverse_lazy("CRM:list_supplier")

'''
The Feedback Views 
'''

class FeedbackCreateView(CreateView):
    model = Feedback 
    fields = ('client_name', 'feedback')
    template_name  = "feedback/feedback_form.html"


class FeedbackUpdateView(UpdateView):
    model = Feedback 
    fields = ('client_name', 'feedback')
    template_name  = "feedback/feedback_form.html"


class FeedbackListView(ListView):
    model = Feedback
    context_object_name  = "feedbacks"
    template_name = "feedback/feedback_list.html"


class FeedbackDeleteView(DeleteView):
    model = Feedback 
    template_name = "feedback/feedback_delete_confirm.html"
    success_url = reverse_lazy("CRM:list_feedback")


class FeedbackDetailView(DetailView):
    model = Feedback 
    context_object_name = "feedback"
    template_name = "feedback/feedback_detail.html"




'''
The Training Feedback 
'''


class TrainingCreateView(CreateView):
    model = Training 
    fields = ('trainer', 'topic', 'number_of_trainee', 'happened_on')
    template_name  = "training/training_form.html"


class TrainingUpdateView(UpdateView):
    model = Training 
    fields = ('trainer', 'topic', 'number_of_trainee', 'happened_on')
    template_name  = "training/training_form.html"


class TrainingListView(ListView):
    model = Training
    context_object_name  = "trainings"
    template_name = "training/training_list.html"


class TrainingDeleteView(DeleteView):
    model = Training 
    template_name = "training/training_confirm_delete.html"
    success_url = reverse_lazy("CRM:list_training")


class TrainingDetailView(DetailView):
    model = Training 
    context_object_name = "training"
    template_name = "training/training_detail.html"
