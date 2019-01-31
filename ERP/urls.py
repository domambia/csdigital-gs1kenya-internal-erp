from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import url, include
from homePage.views import PanelView
from hrm.views import index as hrm_view_index
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_required(PanelView.as_view()), name="index"),
    url(r'^hrm/home/', hrm_view_index, name = "hrm_index"),
    url(r'^leave/', include('leave.urls'), name = "leave"),
    url(r'^departments/', include('departments.urls'), name = "departments"),
    url(r'^hrm/', include('hrm.urls'), name = "hrm"),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^targets/', include('targets.urls')),
    url(r'^crm/', include('CRM.urls')),
    url(r'payroll/', include('payroll.urls')),
]
