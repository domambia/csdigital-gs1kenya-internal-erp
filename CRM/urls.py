from django.conf.urls import url 
from . import views
from django.contrib.auth.decorators import login_required
app_name  = "CRM"

urlpatterns = [
    url(r'^clients/add/', login_required(views.ClientCreateView.as_view()), name = 'create_client'),    
    url(r'^clients/list/', login_required(views.ClientListView.as_view()), name = 'list_client'), 
]
