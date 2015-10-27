from rest_framework import serializers
from .models import Activity, Stat


class ActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Activity
        fields = ('activity_id', 'user_id', 'act_title', 'created_on')


class StatSerializer(serializers.HyperlinkedModelSerializer):
    activity_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True, source='activity')
    class Meta:
        model = Stat
        fields = ('stat_id', 'activity_id', 'count', 'date_done')
