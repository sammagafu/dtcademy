from django.shortcuts import render
from django.views.generic import TemplateView
from course.models import Course
import random

# Create your views here.

class HomePageView(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = Course.objects.all()[:2]
        return context
    
