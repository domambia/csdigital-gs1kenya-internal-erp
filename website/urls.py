from django.conf.urls import url
from . import views


app_name = "website"

urlpatterns = [
    url(r'^about/', views.about, name = "about"),
    url(r'^board-of-directos/', views.bod, name = "bod"),
    url(r'^our-staff/', views.staff, name = "staff"),
]
