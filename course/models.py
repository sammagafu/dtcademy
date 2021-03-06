from email.policy import default
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

    COURSE_LEVEL = [
    ('Beginner', 'Beginner'),
    ('Intermididate', 'Intermididate'),
    ('Expert', 'Expert'),
]


    cover = models.ImageField(verbose_name=_("Course Cover"),upload_to="course/cover/",blank=False,null=False)
    video = models.CharField(max_length=200,blank=False,null=False,verbose_name=_("Intro video"))
    cousername = models.CharField(max_length=50,verbose_name=_("Course Name"))
    category = models.ForeignKey(CourseCategory, verbose_name=_("Course Category"), on_delete=models.DO_NOTHING)
    slug = models.SlugField(_("slug"),editable=False)
    introduction = models.TextField(verbose_name=_("Course Short Brief"))
    price = models.FloatField(verbose_name=_("Course price"))
    description = models.TextField(verbose_name=_("Course Full Description"))
    viewed = models.IntegerField(editable=False,default=0)
    featured = models.BooleanField(_("Featured"),default=False)
    level = models.CharField(max_length=50, verbose_name=_("Course Level"),choices=COURSE_LEVEL,default="Beginner")
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
    course = models.ForeignKey(Course, verbose_name=_(""), on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=160,verbose_name=_("curricullum Name"))
    viewed = models.IntegerField(editable=False,default=0)
    video = models.CharField(max_length=200,blank=False,null=False)
    video_time = models.IntegerField(default=5,verbose_name=_("Video Time"))
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
    course = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.DO_NOTHING)
    downloaded = models.IntegerField(editable=False,default=0)
    title = models.CharField(max_length=50,verbose_name=_("curricullum time"))
    document = models.FileField(verbose_name=_("Documents"),upload_to="course/document/",blank=False,null=False)

    class Meta:
        verbose_name = 'Course Documents'
        verbose_name_plural = 'Courses Documents'

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(CourseDocuments,self).save()