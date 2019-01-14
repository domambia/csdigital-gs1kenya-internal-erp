from django.db import models
from accounts.models import Employee
from datetime import datetime
from django.urls import reverse
# Create your models here.

class Target(models.Model):
    employee = models.ForeignKey(Employee, related_name = "employee", on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    start_date = models.DateField(default =datetime.now)
    end_date = models.DateField()
    status = models.CharField(max_length = 70, default = "incomplete")
    date_of_appraisal = models.CharField(max_length = 40)
    who_appraised = models.CharField(max_length = 80)

    def get_absolute_url(self):
        return reverse("target:target_list")

    def __str__(self):
        return self.name 

    
    


