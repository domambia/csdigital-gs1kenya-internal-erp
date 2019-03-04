from django.conf.urls import url
from ACCNTS import views
app_name  = "ACCNTS"

urlpatterns = [
    url('^dashboard/', views.dashboard, name = "dashboard"),
    url('^invoice/profoma/add/', views.CreateInvoiceView.as_view(), name = 'create_profoma'),
    url('^incoice/profoma/list/', views.ListInvoiceView.as_view(), name ="list_profoma"),
    url('^invoice/profoma/edit/(?P<pk>\d)/$', views.UpdateInvoiceView.as_view(), name ="edit_profoma"),
    url('^invoice/profoma/detail/(?P<pk>\d)/$', views.DetailInvoiceView.as_view(), name ="detail_profoma"),
    url('^invoice/profoma/delete/(?P<pk>\d)/$', views.DeleteInvoiceView.as_view(), name = "delete_profoma"),
]
