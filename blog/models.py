from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django_quill.fields import QuillField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=160)
    slug = models.SlugField(_("slug"),editable=False)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super(Category,self).save()


    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Blog(models.Model):
    title = models.CharField(verbose_name=_("blog"), max_length=160)
    cover  = models.ImageField(verbose_name=_("News Cover"), upload_to="cover/",blank=False,null=False,default="cover.png")
    slug = models.SlugField(_("slug"),editable=False,unique=True)
    brief = models.TextField()
    content = QuillField(null=True,blank=True)
    views=models.IntegerField(default=0)
    published_date = models.DateField(_("Published Date"), auto_now=False, auto_now_add=True)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Blog,self).save()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:detail', args=[str(self.slug)])