from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . models import Blog,Category
# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = "pages/blog.html"
    context_object_name = "blog"



class BlogDetails(DetailView):
    model = Blog
    context_object_name = "blog"
    template_name = "pages/blogDetails.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context