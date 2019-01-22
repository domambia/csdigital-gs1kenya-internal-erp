from django.shortcuts import render
from django.urls import reverse_lazy 
from CRM.models import Client
from helpers.help import get_country, get_sectors
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView 
# Create your views here.

def index(request):

    return "Index"
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

