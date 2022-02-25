from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . models import Course
# Create your views here.


class CourseListView(ListView):
    model = Course
    context_object_name = "course"
    template_name = "pages/course.html"

class CouserDetailView(DetailView):
    model = Course
    context_object_name = "course"
    template_name = "pages/detail.html"