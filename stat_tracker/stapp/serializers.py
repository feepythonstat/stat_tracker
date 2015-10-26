from rest_framework import serializers
from .models import Activity, Stat


class ActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Activity
        fields = ('id', 'user', 'title', 'created_on')


class StatSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stat
        fields = ('id', 'title', 'activity', 'count', 'created_on')
