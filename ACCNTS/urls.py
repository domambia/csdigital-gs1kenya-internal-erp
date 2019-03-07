from django.conf.urls import url
from ACCNTS import views
from ERP import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
app_name  = "ACCNTS"

urlpatterns = [
    url('^dashboard/', views.dashboard, name = "dashboard"),
    url('^invoice/profoma/add/', login_required(views.CreateInvoiceView.as_view()), name = 'create_profoma'),
    url('^incoice/profoma/list/', login_required(views.ListInvoiceView.as_view()), name ="list_profoma"),
    url('^invoice/profoma/edit/(?P<pk>\d)/$', login_required(views.UpdateInvoiceView.as_view()), name ="edit_profoma"),
    url('^invoice/profoma/detail/(?P<pk>\d)/$', login_required(views.DetailInvoiceView.as_view()), name ="detail_profoma"),
    url('^invoice/profoma/delete/(?P<pk>\d)/$', login_required(views.DeleteInvoiceView.as_view()), name = "delete_profoma"),
    url('^invoice/profoma/print/profomaInvoice(?P<pk>\d)/$',login_required(views.print_profoma), name = "print_profoma" ),
    url('^invoice/profoma/payement/(?P<pk>\d)/$',login_required(views.make_payment), name = "payment" ),
    url('^invoice/invoices/list/',login_required(views.list_invoices), name = "invoices" ),
    url('^invoice/profoma/print/invoice/(?P<pk>\d)/$',views.print_invoice, name = "print_invoice" ),
    #payroll
    url('^payroll/add/', login_required(views.CreatePayrollView.as_view()), name = 'create_payroll'),
    url('^payroll/list/', login_required(views.ListPayrollView.as_view()), name ="list_payroll"),
    url('^payroll/edit/(?P<pk>\d)/$', login_required(views.UpdatePayrollView.as_view()), name ="edit_payroll"),
    url('^payroll/generate/(?P<pk>\d)/$', login_required(views.generate_payroll), name ="detail_payroll"),
]+static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
