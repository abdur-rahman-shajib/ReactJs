from rest_framework import serializers

from tourmate.models.enosis_project import EnosisProject

class EnosisProjectSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=30)
    mode = serializers.CharField(required=False, max_length=30)
    client = serializers.CharField(required=False, max_length=30)
    manager = serializers.CharField(required=False, max_length=30)
    lead = serializers.CharField(required=False, max_length=30)
    dev_lead = serializers.CharField(required=False, max_length=30)
    tech_lead = serializers.CharField(required=False, max_length=30)

    se_count = serializers.IntegerField(required=False)
    sse_count = serializers.IntegerField(required=False)
    total_resources = serializers.IntegerField(required=False)
    non_lead_resources = serializers.IntegerField(required=False)
    buffer = serializers.IntegerField(required=False)

    planned = serializers.BooleanField(required=False)
    archived = serializers.BooleanField(required=False)
    

    def create(self, data):
        return EnosisProject(**data)
    
    def update(self, instance, data):
        print(instance.name, 'nnnnnm')
        return instance