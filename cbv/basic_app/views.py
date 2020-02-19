from django.shortcuts import render
from django.views.generic import View , TemplateView ,ListView , DetailView
from . import models
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection!'
        return context


class WorksiteView(ListView):
    context_object_name = 'sites'
    model = models.Worksite

class WorksiteDetailView(DetailView):
    context_object_name = 'sites_detail'
    model = models.Worksite
    template_name = "basic_app/worksite_detail.html"
