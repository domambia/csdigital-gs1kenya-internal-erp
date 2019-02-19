from django.conf.urls import url
from ACCNTS import views
app_name  = "ACCNTS"

urlpatterns = [
    url('^dashboard/', views.dashboard, name = "dashboard"),
]
