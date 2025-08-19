from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'

class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields = '__all__'
        