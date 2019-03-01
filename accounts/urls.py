from django.conf.urls import url
from accounts import views
from django.contrib.auth.decorators import login_required
app_name = 'accounts'

urlpatterns = [
        url(r'^employees/$', views.index, name = "employees"),
        url(r'^add_employee/', views.add_employee, name = 'add_employee'),
        url(r'^profile/(?P<pk>\d+)/$', login_required(views.EmployeeDetailView.as_view()), name = "profile"),
        url(r'^delete/(?P<pk>\d+)/$', views.employee_delete, name = 'employee_delete'),
        url(r'^edit/(?P<pk>\d+)/$', views.employee_update, name = "employee_update"),
        url(r'^user_login/$', views.user_login, name = "login"),
        url(r'^user_logout/$', views.user_logout, name = "logout"),
    ]
