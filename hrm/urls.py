from django.conf.urls import url
from hrm import views

app_name = "hrm"

urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name = "hrm_index")
    ]
