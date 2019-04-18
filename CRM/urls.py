from django.conf.urls import url 
from . import views
from django.contrib.auth.decorators import login_required
app_name  = "CRM"

urlpatterns = [
    #dashboard
    url(r'^dashboard/', login_required(views.index), name = "index"),
    # clients urlpattern 
    url(r'^members/add/', login_required(views.ClientCreateView.as_view()), name = 'create_client'),    
    url(r'^members/list/', views.all_clients, name = 'list_client'), 
    url(r'^members/detail/(?P<pk>\d+)/$', login_required(views.clients), name = 'detail_client'),
    url(r'^members/delete/(?P<pk>\d+)/$', login_required(views.ClientDeleteView.as_view()), name = 'delete_client'),
    url(r'^members/edit/(?P<pk>\d+)/$', login_required(views.ClientUpdateView.as_view()), name = 'edit_client'),
    url(r'^members/approve/ME/(?P<pk>\d+)/$', login_required(views.membership), name = 'me'),
    url(r'^members/approve/TM/(?P<pk>\d+)/$', login_required(views.technical), name = 'tm'),
    url(r'^members/approve/GM/(?P<pk>\d+)/$', login_required(views.general_manager), name = 'gm'),
    url(r'^members/approve/ACCM/(?P<pk>\d+)/$', login_required(views.accounts_manager), name = 'accm'),
    url(r'^members/approve/CACC/(?P<pk>\d+)/$', login_required(views.accounts), name = 'cacc'),
    url(r'^members/notes/add/(?P<pk>\d+)/$', login_required(views.add_notes), name = 'notes'),
    url(r'^members/approve/accounts/Executive/(?P<pk>\d+)/$', login_required(views.accounts_ex), name = 'acc_x'),
    url(r'^members/approve/CCM/(?P<pk>\d+)/$', login_required(views.communication), name = 'ccm'),
    url(r'^members/member_number/(?P<pk>\d+)/$', login_required(views.AssignMemberNumber.as_view()), name = 'assign'),
    url(r'^members/choose_category/(?P<pk>\d+)/$', login_required(views.AddCategoryNumber.as_view()), name="add_category"),
    #suppliers urlpattern
    url(r'^supplier/list/', login_required(views.SupplierListView.as_view()), name = "list_supplier"),
    url(r'^supplier/add/', login_required(views.SupplierCreateView.as_view()), name = 'create_supplier'),
    url(r'^supplier/edit/(?P<pk>\d+)/$', login_required(views.SupplierUpdateView.as_view()), name = 'edit_supplier'),
    url(r'^supplier/detail/(?P<pk>\d+)/$', login_required(views.SupplierDetailView.as_view()), name = 'detail_supplier'),
    url(r'^supplier/delete/(?P<pk>\d+)/$', login_required(views.SupplierDeleteView.as_view()), name = 'delete_supplier'),
    # the feedback  urlpattern
    url(r'^feedback/list/', login_required(views.FeedbackListView.as_view()), name = "list_feedback"),
    url(r'^feedback/add/', login_required(views.FeedbackCreateView.as_view()), name = "create_feedback"),
    url(r'^feedback/detail/(?P<pk>\d+)/$', login_required(views.FeedbackDetailView.as_view()), name = "detail_feedback"),
    url(r'^feedback/delete/(?P<pk>\d+)/$', login_required(views.FeedbackDeleteView.as_view()), name = "delete_feedback"),
    url(r'^feedback/edit/(?P<pk>\d+)/$', login_required(views.FeedbackUpdateView.as_view()), name = "edit_feedback"),
    url(r'^feedback/close/(?P<pk>\d+)/$', views.close, name = "close_feedback"),
    url(r'^feedback/unpend/(?P<pk>\d+)/$', views.unpend, name = "pend_feedback"),
    #training
    url(r'^training/list/', login_required(views.TrainingListView.as_view()), name = "list_training"),  
    url(r'^training/add/', login_required(views.TrainingCreateView.as_view()), name = "create_training"), 
    url(r'^training/detail/(?P<pk>\d+)/$', login_required(views.TrainingDetailView.as_view()), name = "detail_training"), 
    url(r'^training/delete/(?P<pk>\d+)/$', login_required(views.TrainingDeleteView.as_view()), name = "delete_training"), 
    url(r'^training/edit/(?P<pk>\d+)/$', login_required(views.TrainingUpdateView.as_view()), name = "edit_training"), 
    # barcode 
    url(r'^barcode/list/', login_required(views.BarcodeListView.as_view()), name = "list_barcode"),  
    url(r'^barcode/add/', login_required(views.BarcodeCreateView.as_view()), name = "create_barcode"), 
    url(r'^barcode/detail/(?P<pk>\d+)/$', login_required(views.BarcodeDetailView.as_view()), name = "detail_barcode"), 
    url(r'^barcode/delete/(?P<pk>\d+)/$', login_required(views.BarcodeDeleteView.as_view()), name = "delete_barcode"), 
    url(r'^barcode/edit/(?P<pk>\d+)/$', login_required(views.BarcodeUpdateView.as_view()), name = "edit_barcode" ),
    #Event Urls
    url(r'^even/list/', login_required(views.ListEventView.as_view()), name = "list_event"),  
    url(r'^event/add/', login_required(views.CreateEventView.as_view()), name = "create_event"), 
    url(r'^event/detail/(?P<pk>\d+)/$', login_required(views.DetailEventView.as_view()), name = "detail_event"), 
    url(r'^event/delete/(?P<pk>\d+)/$', login_required(views.DeleteEventView.as_view()), name = "delete_event"), 
    url(r'^event/edit/(?P<pk>\d+)/$', login_required(views.UpdateEventView.as_view()), name = "edit_event"),  
]
