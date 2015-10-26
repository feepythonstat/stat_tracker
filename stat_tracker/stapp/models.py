from django.db import models

# Create your models here.


class Activity(models.Model):
    user_id = models.PositiveSmallIntegerField(null=True, blank=True)
    # user = models.ForeignKey(User)
    act_title = models.CharField(max_length=100)
    act_description = models.CharField()
    created_on = models.DateTimeField()


class Stat(models.Model):
    # stat_title = models.CharField(max_length=100)
    activity = models.ForeignKey(Activity)
    count = models.PositiveIntegerField(null=True, blank=True)
    date_done = models.DateTimeField()
