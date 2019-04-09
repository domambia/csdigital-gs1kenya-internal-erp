from django.db import models
from django.urls import reverse
import os, time, random, string
import datetime
from uuid import uuid4
from django.utils.deconstruct import deconstructible
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


file_upload = UploadFolder("documents/legal")

'''
GS1Kenya Registration Deocuments'''

class GS1Docs(models.Model):
    '''
    This is an ORM for GS1 Documents'''
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1000)
    dated  = models.DateField(default=datetime.datetime.now)
    documents = models.FileField(upload_to=file_upload, blank = True)
    status = models.IntegerField(default = 0)

    '''String Name'''
    def __str__(self):
        return self.name

    '''Get absolute url'''
    def get_absolute_url(self):
        return reverse("Legal:gsdocs_list")


'''
Letters Deocuments'''

class Letter(models.Model):
    '''
    This is an ORM for Letter'''
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1000)
    dated  = models.DateField(default=datetime.datetime.now)
    documents = models.FileField(upload_to=file_upload, blank = True)
    status = models.IntegerField(default=0)

    '''String name of the Letters'''
    def __str__(self):
        return self.name

    '''Get absolute url'''
    def get_absolute_url(self):
        return reverse("Legal:letter_list")


    '''
    The Contract Category Model'''

class Category(models.Model):
    '''
    this gives the categories do which the contracts may belong to'''
    name = models.CharField(max_length = 300)
    description = models.CharField(max_length = 1000)
    status = models.IntegerField(default = 0)

    '''String name of the category'''
    def __str__(self):
        return self.name

    '''
    The absolute url
    '''
    def get_absolute_url(self):
        return  reverse("Legal:category_list")

    '''
    The contracts Model'''
class Contract(models.Model):
    '''
    this gives the attributes of the ORM making up the contract model'''
    name  = models.CharField(max_length = 1000)
    dofsigning = models.DateField(default = datetime.datetime.now)
    doflasping = models.DateField(default = datetime.datetime.now)
    category =  models.ForeignKey(Category, on_delete = models.CASCADE, default =1)
    document = models.FileField(upload_to = file_upload, blank = True)
    description = models.CharField(max_length = 1000)
    status = models.IntegerField(default = 0)

    '''String name of the Contracts'''
    def __str__(self):
        return self.name

    '''Get the absolute url for redirections'''
    def get_absolute_url(self):
        return reverse("Legal:contract_list")

