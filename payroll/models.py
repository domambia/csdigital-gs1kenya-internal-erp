from django.db import models
from accounts.models import Employee
import datetime, os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.urls import reverse

# Create your models here.
@deconstructible
class UploadFolder(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


file_upload = UploadFolder("documents/payroll")

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, related_name = "payroll",
                                        on_delete = models.CASCADE
                                )
    payroll_file = models.FileField(upload_to=file_upload,)
    created_on = models.DateField(default = datetime.datetime.now)

    def __str__(self):
        return self.employee 
    def get_absolute_url(self):
        return reverse("payroll:list_payroll")

    

