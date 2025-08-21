from .models import *
from rest_framework import serializers

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
    class Meta:
        model = Music
        fields = '__all__'

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
        