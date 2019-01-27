from django.conf.urls import url 
from . import views
from django.contrib.auth.decorators import login_required
app_name  = "CRM"

urlpatterns = [
    #dashboard
    url(r'^dashboard/', login_required(views.index), name = "index"),
    # clients urlpattern 
    url(r'^clients/add/', login_required(views.ClientCreateView.as_view()), name = 'create_client'),    
    url(r'^clients/list/', login_required(views.ClientListView.as_view()), name = 'list_client'), 
    url(r'^clients/detail/(?P<pk>\d+)/$', login_required(views.ClientDetailView.as_view()), name = 'detail_client'),
    url(r'^clients/delete/(?P<pk>\d+)/$', login_required(views.ClientDeleteView.as_view()), name = 'delete_client'),
    url(r'^clients/edit/(?P<pk>\d+)/$', login_required(views.ClientUpdateView.as_view()), name = 'edit_client'),
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
    #training
    url(r'^training/list/', login_required(views.TrainingListView.as_view()), name = "list_training"),  
    url(r'^training/add/', login_required(views.TrainingCreateView.as_view()), name = "create_training"), 
    url(r'^training/detail/(?P<pk>\d+)/$', login_required(views.TrainingDetailView.as_view()), name = "detail_training"), 
    url(r'^training/delete/(?P<pk>\d+)/$', login_required(views.TrainingDeleteView.as_view()), name = "delete_training"), 
    url(r'^training/edit/(?P<pk>\d+)/$', login_required(views.TrainingUpdateView.as_view()), name = "edit_training"), 

]
