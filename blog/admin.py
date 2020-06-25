from django.contrib import admin

# Register your models here.

from blog import models

from django_summernote.admin import SummernoteModelAdmin

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register([
    models.Author,
    models.Tag,
    models.Like,
    models.Comment,

])

admin.site.register(models.Article, SomeModelAdmin)
