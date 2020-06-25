from django.db import models
from django_mysql.models import ListTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from sortedm2m.fields import SortedManyToManyField

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 256)
    slug = AutoSlugField(populate_from='name', blank = True, editable=True)
    imageurl = models.CharField(max_length = 512, blank = True)
    linkedin_url = models.CharField(max_length = 512, blank = True)
    instagram_url = models.CharField(max_length = 512, blank = True)
    facebook_url = models.CharField(max_length = 512, blank = True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 256)
    slug = AutoSlugField(populate_from='name',  blank = True, editable=True)
    imageurl = models.CharField(max_length = 512, blank = True)
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length = 256)
    slug = AutoSlugField(populate_from='title',  blank = True, editable=True)
    subtitle = models.CharField(max_length = 1024, blank = True)
    createdAt = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    mainauthor = models.ForeignKey('Author', on_delete = models.CASCADE, related_name = 'primary_articles', blank = True)
    other_authors = models.ManyToManyField('Author', related_name = 'other_articles', blank = True)
    imageurl = models.CharField(max_length = 512, blank = True)
    imagecaption = models.CharField(max_length = 256, blank = True)
    tags = models.ManyToManyField('Tag', blank = True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comments')
    article = models.ForeignKey('Article', on_delete = models.CASCADE, related_name = 'comments')
    createdAt = models.DateTimeField(auto_now = True)
    content = models.TextField()


class Like(models.Model):
    article = models.ForeignKey('Article', on_delete = models.CASCADE, related_name = 'likes')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'likes')
    def __str__(self):
        return self.user.first_name + " :  " + self.article.title
