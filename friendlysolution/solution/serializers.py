from rest_framework import serializers
from .models import ImageInfoo

class ImageInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageInfoo
        fields = '__all__'

    
