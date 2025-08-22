from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from music.models import Music

from .models import Comment, Like, Favorite
from .serializers import CommentSerializer, FavoriteSerializer

class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class FavoriteModelViewSet(ModelViewSet):
    queryset = Favorite.objects.order_by('id')
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

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
