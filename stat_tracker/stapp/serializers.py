from rest_framework import serializers
from .models import Activity, Stat


class StatSerializer(serializers.HyperlinkedModelSerializer):
    activity_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True, source='activity')

    class Meta:
        model = Stat
        fields = ('id', 'count', 'date_done', 'activity_id')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    stats = StatSerializer(many=True, read_only=True)

    class Meta:
        model = Activity
        fields = ('id', 'user_id', 'act_title', 'created_on', 'stats')
