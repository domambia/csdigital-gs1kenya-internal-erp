from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import url, include
from homePage.views import index
from hrm.views import index as hrm_view_index
from django.conf import settings
from website.views import indexPage
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_required(index), name="index"),
    url(r'^website/', indexPage, name="website"),
    url(r'^hrm/home/', hrm_view_index, name = "hrm_index"),
    url(r'^leave/', include('leave.urls'), name = "leave"),
    url(r'^departments/', include('departments.urls'), name = "departments"),
    url(r'^hrm/', include('hrm.urls'), name = "hrm"),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^targets/', include('targets.urls')),
    url(r'^crm/', include('CRM.urls')),
        url(r'^legal/', include('Legal.urls')),
    url(r'^ACCNTS/', include('ACCNTS.urls')),
    url(r'^website/', include('website.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)


