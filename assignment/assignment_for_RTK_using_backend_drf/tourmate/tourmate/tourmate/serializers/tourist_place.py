from rest_framework import serializers
import base64

from tourmate.models.tourist_place import TouristPlace
from tourmate.serializers.time_log import TimeLogSerializer


TYPE_OPTIONS = (
        ('beach', 'Beach'),
        ('hill', 'Hill'),
        ('fountain', 'Fountain'),
        ('landmark', 'Landmark'),
    )

class TouristPlaceSerializer(TimeLogSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    address = serializers.CharField(required=True, allow_blank=True, max_length=100)
    place_type = serializers.ChoiceField(choices=TYPE_OPTIONS, default='hill')
    rating = serializers.IntegerField(required=True, min_value=1, max_value=5)
    picture = serializers.CharField(required=False)
    image_file = serializers.ImageField(required=False)

    def getBase64StringFromImage(self, file):
        file_data = base64.b64encode(file.read()).decode('utf-8')
        return f"data:{file.content_type};base64,{file_data}"
    
    def create(self, validated_data):
        print('gffgffgfgggg')
        if validated_data.get('image_file'):
            file = validated_data.pop('image_file')
            encoded_picture = self.getBase64StringFromImage(file)
        else:
            encoded_picture = ''
        print('gdfgdf')
        return TouristPlace(**validated_data, picture = encoded_picture)
    
    def update(self, instance, validated_data):
        print('gffgffgfgggg')
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.place_type = validated_data.get('place_type', instance.place_type)
        instance.rating = validated_data.get('rating', instance.rating)

        img_arr = validated_data.get('image_file')
        if img_arr and len(img_arr):
            file = validated_data.pop('image_file')[0]
            encoded_picture = self.getBase64StringFromImage(file)
        else:
            encoded_picture = instance.picture
    
        instance.picture = encoded_picture
        return instance