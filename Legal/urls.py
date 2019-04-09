from django.conf.urls import url
from . import views, dashboard
from django.contrib.auth.decorators import login_required
app_name  = "Legal"


urlpattern = [
    url(r'^/dashboard', login_required(dashboard.index), name = 'dashboard'),

    # Contracts urls
    url(r'^contract/list/', login_required(views.ContractListView.as_view()), name = "list_event"),
    url(r'^contract/add/', login_required(views.ContractCreateView.as_view()), name = "create_event"),
    url(r'^contract/detail/(?P<pk>\d+)/$', login_required(views.ContractDetailView.as_view()), name = "detail_event"),
    url(r'^contract/delete/(?P<pk>\d+)/$', login_required(views.ContractDeleteView.as_view()), name = "delete_event"),
    url(r'^contract/edit/(?P<pk>\d+)/$', login_required(views.ContractUpdateView.as_view()), name = "edit_event"),

    # the category urls
    url(r'^contract/category/list/', login_required(views.CategoryListView.as_view()), name = "category_list"),
    url(r'^contract/category/add/', login_required(views.CategroyCreateView.as_view()), name = "category_add"),
    url(r'^contract/category/detail/(?P<pk>\d+)/$', login_required(views.CategoryDetailView.as_view()), name = "category_detail"),
    url(r'^contract/category/delete/(?P<pk>\d+)/$', login_required(views.CategoryDeleteView.as_view()), name = "category_delete"),
    url(r'^contract/category/edit/(?P<pk>\d+)/$', login_required(views.CategoryUpdateView.as_view()), name = "category_edit"),

    # gs1Docs urls
    url(r'^documents/list/', login_required(views.GS1DocsListView.as_view()), name = "gs1docs_list"),
    url(r'^documents/add/', login_required(views.GS1DocsCreateView.as_view()), name = "gs1docs_add"),
    url(r'^documents/detail/(?P<pk>\d+)/$', login_required(views.GS1DocsDetailView.as_view()), name = "gs1docs_detail"),
    url(r'^documents/delete/(?P<pk>\d+)/$', login_required(views.GS1DocsDeleteView.as_view()), name = "gs1docs_delete"),
    url(r'^documents/edit/(?P<pk>\d+)/$', login_required(views.GS1DocsUpdateView.as_view()), name = "gs1docs_edit"),
    # Letters Urls
    url(r'^letter/list/', login_required(views.LetterListView.as_view()), name = "letter_list"),
    url(r'^event/add/', login_required(views.CreateEventView.as_view()), name = "letter_add"),
    url(r'^letter/detail/(?P<pk>\d+)/$', login_required(views.LetterDetailView.as_view()), name = "letter_detail"),
    url(r'^letter/delete/(?P<pk>\d+)/$', login_required(views.LetterDelelteView.as_view()), name = "letter_delete"),
    url(r'^letter/edit/(?P<pk>\d+)/$', login_required(views.LetterUpdateView.as_view()), name = "letter_edit"),
]
