from django.db import models
from accounts.models import Employee
from datetime import datetime
from django.urls import reverse
from departments.models import Department
# Create your models here.

class Leave(models.Model):
    name = models.CharField(max_length = 256)
    description = models.CharField(max_length = 256)
    created_on = models.DateField(default = datetime.now)

    def get_absolute_url (self):
        return reverse("leave:leave_list")
    def __str__(self):
        return self.name

def get_clients():
    list_clients = Client.objects.all()
    clients = []
    for cl in list_clients:
        clients.append((cl.id, cl.company_name ,))
    return tuple(clients)


def get_leaves():
    list_leaves = Leave.objects.all()
    leaves = []
    for cl in list_leaves:
        leaves.append((cl.id, cl.name ,))
    return tuple(leaves)

def get_employees():
    list_employees = Employee.objects.all()
    employees = []
    for cl in list_employees:
        leaves.append((cl.id, cl.user.first_name + cl.user.last_name  ,))
    return tuple(employees)

class ApplyLeave(models.Model):
    start_date = models.DateField()
    status = models.IntegerField(default = 0)
    end_date = models.DateField()
    resume_date = models.DateField()
    person_taking_charge = models.ForeignKey(Employee, related_name = "person_taking",
                                        on_delete = models.CASCADE, default=1
                                )
    employee = models.CharField(max_length =200)
    home_phone = models.CharField(max_length = 20)
    leave = models.ForeignKey(Leave, related_name = "leave", on_delete = models.CASCADE, default=1)

    def get_absolute_url (self):
        return reverse("leave:applyleave_list")

    def __str__(self):
        return self.leave.name
