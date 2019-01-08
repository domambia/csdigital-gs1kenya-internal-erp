from django.conf.urls import url
from departments import views
from django.contrib.auth.decorators import login_required

app_name = "departments"

urlpatterns = [
            url(r'^add/', login_required(views.CreateDepartmentView.as_view()), name = "add_department" ),
            url(r'^$', login_required(views.ListDepartmentsView.as_view()), name = "list_department" ),
            url(r'^edit/(?P<pk>\d+)/$', login_required(views.UpdateDepartmentView.as_view()), name = "edit_department" ),
            url(r'^show/(?P<pk>\d+)/$', login_required(views.DetailDepartmentView.as_view()), name = "show_department" ),
            url(r'^delete/(?P<pk>\d+)/$', login_required(views.DeleteDepartmentView.as_view()), name = "delete_department" ),

            url(r'^positions/add/', login_required(views.CreatePositionView.as_view()), name = "add_position" ),
            url(r'^positions/$', login_required(views.ListPositionView.as_view()), name = "list_position" ),
            url(r'^positions/edit/(?P<pk>\d+)/$', login_required(views.UpdatePositionView.as_view()), name = "edit_position" ),
            url(r'^positions/show/(?P<pk>\d+)/$', login_required(views.DetailPositionView.as_view()), name = "show_position" ),
            url(r'^positions/delete/(?P<pk>\d+)/$', login_required(views.DeletePositionView.as_view()), name = "delete_position" ),

        ]
