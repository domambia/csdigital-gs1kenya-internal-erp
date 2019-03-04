from django.db import models
from CRM.models import Client
import datetime
from django.urls import reverse
# Create your models here.

class Invoice(models.Model):
    OPTIONS =(
        ("Yes", "Yes"),
        ("No", "No"),
    )
    member = models.ForeignKey(Client, on_delete = models.CASCADE,  default = 1)
    date_of_generate = models.DateField(default = datetime.datetime.now)
    description = models.CharField(max_length=2000)
    VAT = models.CharField(max_length = 5, choices = OPTIONS, default = "No")
    def __str__(self):
        return self.member.company_name

    def get_absolute_url(self):
        return reverse("ACCNTS:list_profoma")
