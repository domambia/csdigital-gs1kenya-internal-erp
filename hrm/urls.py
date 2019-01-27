from django.conf.urls import url
from hrm import views

app_name = "hrm"

urlpatterns = [
        url(r'^$', views.index, name = "hrm_index")
    ]
