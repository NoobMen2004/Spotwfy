from .models import *
from rest_framework import serializers
from django.db.models import Avg, Count

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def get_music(self, instance):
        musics = instance.music.all()
        return MusicSerializer(musics, many=True).data

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['music'] = self.get_music(instance)
        return repr

class MusicSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    ratings_count = serializers.SerializerMethodField()

    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ['user']

    def get_avg_rating(self, obj):
        avg = obj.ratings.aggregate(avg=Avg('score'))['avg']
        return round(avg, 2) if avg else None

    def get_ratings_count(self, obj):
        return obj.ratings.aggregate(count=Count('id'))['count']

    def validate_music(self, value):
        valid_file_types = ['audio/mpeg', 'audio/wav', 'audio/ogg']
        if value.content_type not in valid_file_types:
            raise serializers.ValidationError('Только аудио файлы (mp3, wav, ogg) разрешены.')
        return value

class PlayListSerializer(serializers.ModelSerializer):
    music = serializers.SlugRelatedField(
        many = True,
        read_only = True,
        slug_field = 'title'
    )
    class Meta:
        model = PlayList
        fields = '__all__'
        read_only_fields = ['user'] 
        