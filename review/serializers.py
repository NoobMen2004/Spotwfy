from rest_framework import serializers
from .models import Comment, Favorite, Rating
from music.serializers import MusicSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'music', 'body', 'created_at']
        read_only_fields = ['user']

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['user'] = {
            'id': instance.user.id,
            'email': instance.user.email
        }
        repr['music'] = {
            'id': instance.music.id,
            'title': instance.music.title
        }
        return repr

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'music', 'created_at']
        read_only_fields = ['user']

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['music'] = MusicSerializer(instance.music).data
        return repr

class RatingSerializer(serializers.ModelSerializer):
    star = serializers.IntegerField(source='score') 

    class Meta:
        model = Rating
        fields = ['id', 'music', 'star']
        read_only_fields = ['user']

    def validate_star(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError('Рейтинг должен быть от 1 до 5')
        return value