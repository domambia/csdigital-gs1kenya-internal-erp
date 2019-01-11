from django.db import models
from accounts.models import Employee
from datetime import datetime
from django.urls import reverse
from departments.models import Department
# Create your models here.

class Leave(models.Model):
    name = models.CharField(max_length = 256)
    description = models.CharField(max_length = 256)
    period = models.PositiveIntegerField(default = 3)
    created_on = models.DateField(default = datetime.now)

    def get_absolute_url (self):
        return reverse("leave:leave_list")
    def __str__(self):
        return self.name


class ApplyLeave(models.Model):
    start_date = models.DateField()
    status = models.IntegerField(default = 0)

    end_date = models.DateField()
    resume_date = models.DateField(default = "1/1/2018")
    person_taking_charge = models.ForeignKey(Employee, related_name ="person_charge",
                                        on_delete = models.CASCADE, default ="hr"
                                    ) # From here take his phone number and other details 
    employee = models.ForeignKey(Employee, related_name = "employees",
                                        on_delete = models.CASCADE
                                )
    home_phone = models.IntegerField()
    leave = models.ForeignKey(Leave, related_name = "leave",
                                        on_delete = models.CASCADE
                                )
    def get_absolute_url (self):
        return reverse("leave:applyleave_list")

    def __str__(self):
        return self.leave.name
