from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from course.models import Course
from blog.models import Blog
import random

# Create your views here.

class HomePageView(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = Course.objects.all()[:2]
        context["blog"] = Blog.objects.all()[:3]
        return context
    
class Contact(View):
    template_name = 'pages/contact.html'
    def get(self, request):
        return render(request,self.template_name)

    def post(self,request):
        return render(request,self.template_name)