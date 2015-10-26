from django.db import models

# Create your models here.


class Activity(models.Model):
    user = models.PositiveSmallIntegerField(null=True, blank=True)
    # user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    created_on = models.DateTimeField()


class Stat(models.Model):
    title = models.CharField(max_length=100)
    activity = models.ForeignKey(Activity)
    count = models.PositiveIntegerField(null=True, blank=True)
    created_on = models.DateTimeField()
