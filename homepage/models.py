from django.db import models
from django_mysql.models import ListTextField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class TechPeCharchaEpisodes(models.Model):
    title = models.CharField(max_length = 256)
    date = models.DateField()
    description = models.TextField()
    youtubelink = models.CharField(max_length = 256)
    def __str__(self):
        return self.title

class PublicSpeakingEvents(models.Model):
    title = models.CharField(max_length = 256)
    date = models.DateField()
    venue = models.CharField(max_length = 256)
    description = models.TextField()
    youtubelink = models.CharField(max_length = 256, blank=True,  default='')
    images = ListTextField(
        base_field= models.CharField(max_length = 512),
        size=15,
        blank=True
    )
    staticimages = ListTextField(
        base_field= models.CharField(max_length = 512),
        size=10,
        blank=True
    )
    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length = 256)
    description = models.TextField(blank = True)
    imageurl = models.CharField(max_length = 512, blank = True)
    rating = models.DecimalField(decimal_places=1, max_digits = 3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    def __str__(self):
        return self.title
