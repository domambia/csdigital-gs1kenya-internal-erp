from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# Create your views here.


class PanelView(TemplateView):

    template_name = "homePage/index.html"
