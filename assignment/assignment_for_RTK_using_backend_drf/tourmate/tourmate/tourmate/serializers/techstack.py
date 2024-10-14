from rest_framework import serializers

from tourmate.models.techstack import TechStack

class TechStackSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=30)
    code = serializers.CharField(required=False, max_length=30)
    

    def create(self, data):
        return TechStack(**data)
    
    def update(self, instance, data):
        return instance