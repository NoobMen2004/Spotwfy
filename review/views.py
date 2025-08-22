from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .serializers import CommentSerializer, FavoriteSerializer, RatingSerializer

from music.models import Music
from .models import *
from music.permission import IsOwner

class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoriteModelViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RatingModelViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['POST'])
def toogle_like(request, id):
    user = request.user
    if not user.is_authenticated:
        return Response(status=401)
    music = get_object_or_404(Music, id=id)
    if Like.objects.filter(user=user, movies=music).exists():
        Like.objects.filter(user=user, movies=music).delete()
    else:
        Like.objects.create(user=user, music=music)
    return Response(status=201)