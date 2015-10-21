# rango/models


from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.views < 0:
            self.views = 0
        if self.likes < 0:
            self.likes = 0
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Page(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.user.username



