from django.conf.urls import url
from hrm import views
from django.contrib.auth.decorators import login_required

app_name = "hrm"

urlpatterns = [
        url(r'^$', views.index, name = "hrm_index"),
        url(r'^performance/list/$', login_required(views.ListPerformanceView.as_view()), name='perfom_list'),
        url(r'^performance/add/$', login_required(views.CreatePerformanceView.as_view()), name='perfom_add'),
        url(r'^performance/detail/(?P<pk>\d+)/$', login_required(views.DetailPerformanceView.as_view()), name='perfom_detail'),
        url(r'^performance/delete/(?P<pk>\d+)/$', login_required(views.DeletePerformanceView.as_view()), name='perfom_delete'),
        url(r'^performance/edit/(?P<pk>\d+)/$', login_required(views.UpdatePerformanceView.as_view()), name='perfom_edit'),
        url(r'^own/performance/list/$', login_required(views.show_employee_perfomance_control), name='perfom_employee'),
        url(r'^performance/notes/(?P<pk>\d+)/$', login_required(views.perfomance_notes), name='perfom_note'),
        url(r'^performance/appraise/(?P<pk>\d+)/$', login_required(views.appraisal), name='appraise'),
    ]
