from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Goal(models.Model):
    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    details = models.CharField(default='', blank=True, max_length=300)
    description = models.CharField(max_length=300, default='')
    frequency = models.CharField(max_length=100, default='')
    startDate = models.DateTimeField(blank=True)
    endDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}s goal of {self.name}"


class Tracker(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    doneday = models.DateTimeField(auto_now=True)
    notes = models.CharField(default='', blank=True, max_length=300)

    def __str__(self):
        return f"tracker for {self.goal} made on {self.doneday.day}st of {self.doneday.month} "


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media')
