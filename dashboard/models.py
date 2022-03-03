from django.db import models
from django.conf import settings 
from course.models import Course
from django.utils.translation import gettext as _
# Create your models here.

class EnrolledCourse(models.Model):
    enrolled_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    enrolled_course = models.ForeignKey(Course,on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("EnrolledCourse")
        verbose_name_plural = _("EnrolledCourses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("EnrolledCourse_detail", kwargs={"pk": self.pk})
