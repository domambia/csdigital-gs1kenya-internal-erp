from django.conf.urls import url 
from payroll import views 

app_name = "payroll"

urlpatterns = [
    url(r'^list/', views.PayrollListView.as_view(), name = "list_payroll"),
    url(r'^add/', views.PayrollCreateView.as_view(), name = "create_payroll"),
    url(r'^edit/(?P<pk>\d+)/$', views.PayrollUpdateView.as_view(), name = "edit_payroll"),
    url(r'^details/(?P<pk>\d+)/$', views.PayrollDetailView.as_view(), name = "detail_payroll"),
    url(r'^delete/(?P<pk>\d+)/$', views.PayrollDeleteView.as_view(), name = "delete_payroll"),
]
