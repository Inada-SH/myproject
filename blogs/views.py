from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

class IndexTemplateView(TemplateView):
    template_name = "index.html"

class CreateTemplateView(TemplateView):
    template_name = "create.html"