from django.conf.urls import url
from . import views


app_name = "website"

urlpatterns = [
    url(r'^about/', views.about, name = "about"),
    url(r'^board-of-directos/', views.bod, name = "bod"),
    url(r'^our-staff/', views.staff, name = "staff"),
    url(r'^contact/', views.contact, name = "contact"),
    url(r'^our-standards/',  views.standards, name='standards'),
    url(r'^our-memoradum/', views.memoradum, name = "memoradum"),
    url(r'^our-history/', views.history, name="history"),
    url(r'^our-identify/', views.identity, name = "identity"),

]
