from django.db import models
from account.models import CustomUser

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Music(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='music_owner')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media_music')
    image = models.ImageField(upload_to='media_image',blank=True)
    description = models.TextField(blank=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='music')
    create_add = models.DateTimeField(auto_now_add=True)
    update_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PlayList(models.Model):
    title = models.CharField(max_length=255)
    music = models.ManyToManyField(Music, related_name='playlist', blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    create_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title