from django.db import models
from django.urls import reverse
from helpers.help import get_country, get_sectors, get_categs
# Create your models here.

def client_file_folder(client_name):

    return 'documents/{0}/'.format(client_name)


class Client(models.Model):
    company_name = models.CharField(max_length = 100)
    company_phone = models.IntegerField()
    company_phone_alt = models.IntegerField()
    company_email = models.CharField(max_length = 128)
    company_email_alt = models.CharField(max_length = 128)
    post_address = models.CharField(max_length = 200)
    physical_location = models.CharField(max_length = 60)
    director_info = models.CharField(max_length = 1000)
    sector = models.CharField(max_length = 200, choices = get_sectors(), default = "No sector")
    category = models.CharField(max_length = 80, choices = get_categs(), default = "No category")
    date_of_issue = models.DateField()
    nature_of_business = models.CharField(max_length =100)

    # documents 
    certificate_of_incorporation = models.FileField(upload_to = client_file_folder(company_name), blank = True)
    copy_of_id = models.FileField(upload_to = client_file_folder(company_name), blank = True)
    copy_of_blank_cheque = models.FileField(upload_to = client_file_folder(company_name), blank = True)
    copy_of_trade_licence = models.FileField(upload_to = client_file_folder(company_name), blank = True)
    list_of_product_barcoded = models.FileField(upload_to = client_file_folder(company_name), blank = True)
    director_pin_number = models.FileField(upload_to = client_file_folder(company_name), blank = True)
    company_certificate_pin = models.FileField(upload_to = client_file_folder(company_name), blank = True)
    copy_of_kebs_certicate = models.FileField(upload_to = client_file_folder(company_name), blank = True)
    
    def get_absolute_url(self):
        return reverse("CRM:list_client")

    def __str__(self):
        return self.company_name

class Supplier(models.Model):
    name = models.CharField(max_length = 100)
    phone  = models.IntegerField()
    country = models.CharField(max_length = 40, choices = get_country())
    website = models.URLField(blank = True)
    description = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name


