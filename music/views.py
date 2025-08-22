from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg, Count

from .permission import IsOwner
from .models import Category, Music, PlayList
from .serializers import CategorySerializer, MusicSerializer, PlayListSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['title']

class MusicViewSet(ModelViewSet):
    queryset = Music.objects.all().annotate(
        avg_rating=Avg('ratings__score'),
        ratings_count=Count('ratings')
    )
    serializer_class = MusicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['cat']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PlayListViewSet(ModelViewSet):
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)