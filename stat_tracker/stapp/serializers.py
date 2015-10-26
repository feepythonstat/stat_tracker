from rest_framework import serializers
from .models import Activity, Stat


class ActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Activity
        fields = ('activity_id', 'user_id', 'act_title', 'created_on')


class StatSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stat
        fields = ('stat_id', 'activity_id', 'count', 'date_done')
