from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg, Count
from django.core.cache import cache

from .permission import IsOwner, IsAdminOrReadOnly
from .models import Category, Music, PlayList
from .serializers import CategorySerializer, MusicSerializer, PlayListSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['title']

class MusicViewSet(ModelViewSet):
    serializer_class = MusicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def get_queryset(self):
        musics = cache.get('musics')
        if not musics:
            musics = Music.objects.annotate(
                avg_rating=Avg('ratings__score'),
                ratings_count=Count('ratings')
            )
            cache.set('musics', musics, 60*5)
        return musics

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        cache.delete('musics')

class PlayListViewSet(ModelViewSet):
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)