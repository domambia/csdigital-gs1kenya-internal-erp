from django.contrib import admin
from .models import Category, GS1Docs, Contract, Letter
# Register your models here.

admin.site.register(Category)
admin.site.register(Letter)
admin.site.register(GS1Docs)
admin.site.register(Contract)
