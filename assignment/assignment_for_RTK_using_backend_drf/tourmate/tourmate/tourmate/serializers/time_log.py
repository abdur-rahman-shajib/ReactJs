from rest_framework import serializers


class TimeLogSerializer(serializers.Serializer):
    created_at = serializers.CharField(required=False, allow_blank=True, max_length=100)
    updated_at = serializers.CharField(required=False, allow_blank=True, max_length=100)
    