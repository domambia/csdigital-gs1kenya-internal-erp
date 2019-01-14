from django.conf.urls import url 
from . import views 

app_name = "target"

urlpatterns = [
    url(r'list', views.TargetListView.as_view(), name = "target_list"),
    url(r'create', views.TargetCreateView.as_view(), name = "target_create"),
    url(r'edit/(?P<pk>\d+)/$', views.TargetUpdateView.as_view(), name = "target_edit"),
    url(r'detail/(?P<pk>\d+)/$', views.TargetDetailView.as_view(), name = "target_detail"),
    url(r'delete/(?P<pk>\d+)/$', views.TargetDeleteView.as_view(), name = "target_delete"),
]
