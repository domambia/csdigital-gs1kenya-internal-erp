from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length = 256)
    initials = models.CharField(max_length =20)
    created_on = models.DateField(default = datetime.now)

    def get_absolute_url(self):

        return reverse("departments:list_department")
        
    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length = 256)
    department = models.ForeignKey("Department", related_name = "depart", on_delete=models.CASCADE, default=3)
    initials = models.CharField(max_length =20)
    def get_absolute_url(self):
        return reverse("departments:list_position")

    def __str__(self):
        return self.name
