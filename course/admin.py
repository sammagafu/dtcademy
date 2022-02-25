from django.contrib import admin
from .models import Course,CourseCurricullum,CourseDocuments,CourseCategory
# Register your models here.
admin.site.register(Course)
admin.site.register(CourseCurricullum)
admin.site.register(CourseDocuments)
admin.site.register(CourseCategory)