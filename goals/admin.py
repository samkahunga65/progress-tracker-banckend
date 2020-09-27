from django.contrib import admin
from .models import Goal, Tracker, UserProfile
# Register your models here.
admin.site.register(Goal)
admin.site.register(Tracker)
admin.site.register(UserProfile)
