from django.db import models
import datetime

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField(max_length=300, verbose_name='Content')
    email = models.EmailField(max_length=200, verbose_name='Email')
    datetime = models.DateTimeField(default=datetime.datetime.now())
    url = models.URLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)


    def __str__(self):
        return self.name


