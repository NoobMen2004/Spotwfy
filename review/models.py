from django.db import models
from django.contrib.auth import get_user_model

from music.models import Music

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True) 

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='likes')

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite')
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='favorite')

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveSmallIntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'music') 
