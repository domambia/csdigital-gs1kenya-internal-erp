from django.conf.urls import url
from ACCNTS import views
from ERP import settings
from ACCNTS import vsales, accounts
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from ACCNTS import vexpenses, reports
app_name  = "ACCNTS"

urlpatterns = [
    url('^dashboard/', views.dashboard, name = "dashboard"),
    url('^invoice/profoma/add/', login_required(views.CreateInvoiceView.as_view()), name = 'create_profoma'),
    url('^incoice/profoma/list/', login_required(views.ListInvoiceView.as_view()), name ="list_profoma"),
    url('^invoice/profoma/edit/(?P<pk>\d)/$', login_required(views.UpdateInvoiceView.as_view()), name ="edit_profoma"),
    url('^invoice/profoma/detail/(?P<pk>\d)/$', login_required(views.DetailInvoiceView.as_view()), name ="detail_profoma"),
    url('^invoice/profoma/delete/(?P<pk>\d)/$', login_required(views.DeleteInvoiceView.as_view()), name = "delete_profoma"),
    url('^invoice/profoma/print/profomaInvoice(?P<pk>\d)/$',login_required(views.print_profoma), name = "print_profoma" ),
    # not working
    url('^invoice/profoma/payement/(?P<pk>\d)/$',login_required(views.make_payment), name = "payment" ),
    url('^invoice/invoices/list/',login_required(views.list_invoices), name = "invoices" ),
    url('^invoice/profoma/print/invoice/(?P<pk>\d)/$',views.print_invoice, name = "print_invoice" ),

    # payment
    url('^payment/delete/(?P<pk>\d)/$',login_required(views.DeletePaymentView.as_view()), name = "payment_delete" ),
    url('^payment/list/',login_required(views.ListPaymentView.as_view()), name = "payment_list" ),
    url('^payment/detail/(?P<pk>\d)/$',login_required(views.DetailPaymentView.as_view()), name = "payment_detail"),
    url('^payment/pay/',login_required(views.CreatePaymentView.as_view()), name='payment_create'),
    url(r'^payment/edit/(?P<pk>\d+)/$', login_required(views.UpdatePaymentView.as_view()), name = "payment_edit"),
    #payroll
    url('^payroll/add/', login_required(views.CreatePayrollView.as_view()), name = 'create_payroll'),
    url('^payroll/list/', login_required(views.ListPayrollView.as_view()), name ="list_payroll"),
    url('^payroll/edit/(?P<pk>\d)/$', login_required(views.UpdatePayrollView.as_view()), name ="edit_payroll"),
    url('^payroll/generate/(?P<pk>\d)/$', login_required(views.generate_payroll), name ="detail_payroll"),
    url('^payslip/list/', login_required(views.payslip), name ="payslip"),
    url('^payroll/tax/(?P<tax_id>\d)/$', login_required(views.post_deductions), name ="tax"),
    #sales

    url('^sales/list/', login_required(vsales.ListSalesView.as_view()), name = 'sales_list'),
    url('^sales/create/', login_required(vsales.CreateSalesView.as_view()), name = 'sales_add'),
    url('^sales/edit/(?P<pk>\d+)/$', login_required(vsales.UpdateSalesView.as_view()), name = 'sales_edit'),
    url('^sales/details/(?P<pk>\d+)/$', login_required(vsales.DetailSalesView.as_view()), name = 'sales_detail'),
    url('^sales/delete/(?P<pk>\d+)/$', login_required(vsales.DeleteSalesView.as_view()), name = 'sales_delete'),

    # expenses
    url(r'^purchases/list/', login_required(vexpenses.ListExpenseView.as_view()), name="expense_list"),
    url(r'^purchases/create/', login_required(vexpenses.CreateExpenseView.as_view()), name="expense_add"),
    url(r'^purchases/delete/(?P<pk>\d+)/$', login_required(vexpenses.DeleteExpenseView.as_view()), name="expense_delete"),
    url(r'^purchases/detail/(?P<pk>\d+)/$', login_required(vexpenses.DetailExpenseView.as_view()), name="expense_detail"),
    url(r'^purchases/edit/(?P<pk>\d+)/$', login_required(vexpenses.UpdateExpenseView.as_view()), name="expense_edit"),

    ## accounts
    #asset
    url(r'^assets/list/', login_required(accounts.AssetListView.as_view()), name = "asset_list"),
    url(r'^assets/create/', login_required(accounts.AssetCreateView.as_view()), name = "asset_add"),
    url(r'^assets/edit/(?P<pk>\d+)/$', login_required(accounts.AssetUpdateView.as_view()), name = "asset_edit"),
    url(r'^assets/delete/(?P<pk>\d+)/$', login_required(accounts.AssetDeleteView.as_view()), name = "asset_delete"),
    url(r'^assets/detail/(?P<pk>\d+)/$', login_required(accounts.AssetDetailView.as_view()), name = "asset_detail"),

    #Income
    url(r'^income/list/', login_required(accounts.IncomeListView.as_view()), name = "income_list"),
    url(r'^income/create/', login_required(accounts.IncomeCreateView.as_view()), name = "income_add"),
    url(r'^income/edit/(?P<pk>\d+)/$', login_required(accounts.IncomeUpdateView.as_view()), name = "income_edit"),
    url(r'^income/delete/(?P<pk>\d+)/$', login_required(accounts.IncomeDeleteView.as_view()), name = "income_delete"),
    url(r'^income/detail/(?P<pk>\d+)/$', login_required(accounts.IncomeDetailView.as_view()), name = "income_detail"),

    #liability
    url(r'^liability/list/', login_required(accounts.LiabilityListView.as_view()), name = "liability_list"),
    url(r'^liability/create/', login_required(accounts.LiabilityCreateView.as_view()), name = "liability_add"),
    url(r'^liability/edit/(?P<pk>\d+)/$', login_required(accounts.LiabilityUpdateView.as_view()), name = "liability_edit"),
    url(r'^liability/delete/(?P<pk>\d+)/$', login_required(accounts.LiabilityDeleteView.as_view()), name = "liability_delete"),
    url(r'^liability/detail/(?P<pk>\d+)/$', login_required(accounts.LiabilityDetailView.as_view()), name = "liability_detail"),

    url(r'^banking/list/', login_required(accounts.BankListView.as_view()), name = "bank_list"),
    url(r'^banking/create/', login_required(accounts.BankCreateView.as_view()), name = "bank_add"),
    url(r'^banking/edit/(?P<pk>\d+)/$', login_required(accounts.BankUpdateView.as_view()), name = "bank_edit"),
    url(r'^banking/delete/(?P<pk>\d+)/$', login_required(accounts.BankDeleteView.as_view()), name = "bank_delete"),
    url(r'^banking/detail/(?P<pk>\d+)/$', login_required(accounts.BankDetailView.as_view()), name = "bank_detail"),

    # Reports
    url(r'reports/sales/', reports.sales_report, name ='sales_report'),
    url(r'reports/banking/', reports.banking_report, name ='banking_report'),
    url(r'reports/purchases/', reports.expenses_report, name ='expense_report'),
    url(r'reports/fixed-assets/', reports.fixed_asset_report, name = 'asset_report'),
    url(r'reports/profit-and-loss-report/', reports.profit_and_loss_report, name = 'p_loss_report'),
    url(r'reports/kra-reports/', reports.kra_report, name = 'kra_report'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_DIR)









