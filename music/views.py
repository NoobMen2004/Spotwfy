from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .permission import IsOwner
from .models import *
from .serializer import *

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class MusicViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PlayListViewSet(ModelViewSet):
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
