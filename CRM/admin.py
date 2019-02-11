from django.contrib import admin
from CRM.models import Client, Supplier, Training, Feedback

# Register clients and design it well
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass



@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'country', 'website', 'description')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass 

# the Training panel 
@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    pass