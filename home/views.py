from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Shakti Electricals'   #  like a default dictionary 
        context['tagLine'] = 'Professional Electrical Solutions'
        context['contact'] = 'Emergency: (555) 123-4567'
        return context



