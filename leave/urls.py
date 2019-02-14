from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = "leave"

urlpatterns = [
        url(r'^list/', views.LeaveListView.as_view(), name = "leave_list"),
        url(r'^add/', views.LeaveCreateView.as_view(), name = "add_leave"),
        url(r'^edit/(?P<pk>\d+)/$', views.LeaveUpdateView.as_view(), name = "leave_edit"),
        url(r'^delete/(?P<pk>\d+)/$', views.LeaveDeleteView.as_view(), name = "leave_delete"),
        url(r'^show/(?P<pk>\d+)/$', views.LeaveDetailView.as_view(), name = "leave_detail"),
        url(r'^apply/', views.applyleave, name = "apply_leave"),
        url(r'^applied_leaves/', views.ApplyLeaveListView.as_view(), name = "applyleave_list"),
        url(r'^applied_leave_edit/(?P<pk>\d+)/$',login_required(views.ApplyLeaveUpdateView.as_view()), name = "applied_lv_edit"),
        url(r'^approve/(?P<pk>\d+)/$', views.approve_leave, name = "approve"),
        url(r'^download/(?P<pk>\d+)/$', views.render_pdf_docs, name = "download_leave"),
    ]
