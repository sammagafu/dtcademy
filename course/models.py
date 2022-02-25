from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify

# Create your models here.

class CourseCategory(models.Model):
    title = models.CharField(max_length=160,verbose_name=_("Course Category"))
    slug = models.SlugField(_("slug"),editable=False)


    def __str__(self):
        return self.title


    def save(self):
        self.slug = slugify(self.title)
        super(CourseCategory,self).save()

    class Meta:
        verbose_name = 'Course Category'
        verbose_name_plural = 'Courses Categories'

class Course(models.Model):
    cover = models.ImageField(verbose_name=_("Course Cover"),upload_to="course/cover/",blank=False,null=False)
    video = models.CharField(max_length=200,blank=False,null=False,verbose_name=_("Intro video"))
    cousername = models.CharField(max_length=50,verbose_name=_("Course Name"))
    category = models.ForeignKey(CourseCategory, verbose_name=_("Course Category"), on_delete=models.CASCADE)
    slug = models.SlugField(_("slug"),editable=False)
    introduction = models.TextField(verbose_name=_("Course Short Brief"))
    price = models.FloatField(verbose_name=_("Course price"))
    description = models.TextField(verbose_name=_("Course Full Description"))
    viewed = models.IntegerField(editable=False,default=0)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return self.cousername

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("course:detail", kwargs={"slug": self.slug})


    def save(self):
        self.slug = slugify(self.cousername)
        super(Course,self).save()

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'



class CourseCurricullum(models.Model):
    title = models.CharField(max_length=160,verbose_name=_("curricullum time"))
    viewed = models.IntegerField(editable=False,default=0)
    video = models.CharField(max_length=200,blank=False,null=False)
    slug = models.SlugField(_("slug"),editable=False)

    class Meta:
        verbose_name = 'Course Curricullum'
        verbose_name_plural = 'Courses Curricullum'

    
    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(CourseCurricullum,self).save()


class CourseDocuments(models.Model):
    downloaded = models.IntegerField(editable=False,default=0)
    title = models.CharField(max_length=50,verbose_name=_("curricullum time"))
    document = models.FileField(verbose_name=_("Documents"),upload_to="course/document/",blank=False,null=False)
    course = models.ForeignKey(CourseCurricullum, verbose_name=_("curricullum document"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Course Documents'
        verbose_name_plural = 'Courses Documents'

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(CourseDocuments,self).save()