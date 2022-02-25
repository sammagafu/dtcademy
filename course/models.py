from django.db import models

# Create your models here.
class Course(models.Model):

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'