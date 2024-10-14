from rest_framework import serializers

from tourmate.serializers.time_log import TimeLogSerializer
from tourmate.serializers.tourist_place import TouristPlaceSerializer


class UserSerializer(TimeLogSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, allow_blank=False, max_length=30)
    touristplaces = TouristPlaceSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        return instance