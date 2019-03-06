from django.db import models
from accounts.models import Employee 
import datetime 
from django.urls import reverse
# Create your models here.
class Performance(models.Model):
    employee = models.ForeignKey(Employee, related_name='target', on_delete = models.CASCADE, default= 1)
    start_date  = models.DateField(default =datetime.datetime.now)
    finish_date = models.DateField()
    objective = models.CharField(max_length =200)
    notes = models.CharField(max_length=1000, blank = True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.employee.user.username 
    def get_absolute_url(self):
        return reverse("hrm:perfom_list")

    