from celery import shared_task
from django.db.models import Avg
from music.models import Music
from django.core.cache import cache

@shared_task
def update_avg_rating(music_id):
    music = Music.objects.get(id=music_id)
    avg = music.ratings.aggregate(avg_score=Avg('score'))['avg_score'] or 0
    music.avg_rating = avg
    music.save()
    cache.delete('musics')
