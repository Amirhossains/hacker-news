from django.contrib import admin

from .models import *

admin.site.register(NewsItem)
admin.site.register(NewsVote)
admin.site.register(NewsStory)
admin.site.register(NewsComment)
