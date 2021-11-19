from django.contrib import admin
from Profiles_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
