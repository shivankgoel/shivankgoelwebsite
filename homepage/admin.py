from django.contrib import admin

# Register your models here.
from homepage import models

admin.site.register([
    models.TechPeCharchaEpisodes,
    models.PublicSpeakingEvents,
    models.Book,
    models.YoutubeLinks,
])
