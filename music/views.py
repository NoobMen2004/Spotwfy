

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status


from .models import *
from .serializer import *


class CategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializers = CategorySerializer(data = request.data)
        if serializers.is_valid():
            cat = serializers.save()
            return Response({
                'data':serializers.data, 
                'message':f'Категория {cat.title} добавлено.'
                })
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        cat = Category.objects.all()
        serializers = CategorySerializer(cat, many=True)
        return Response(serializers.data)
    
    def put(self, request, id):
        cat = Category.object.get(pk=id)
        serializers = CategorySerializer(cat, data = request.data)
        if serializers.is_valid():
            cat = serializers.save()
            return Response({
                'data': serializers.data,
                'message':f'Категория {cat.title} измененно'
            })


class MusicAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializers = MusicSerializer(data = request.data)
        serializers.is_valid(raise_exception=True)
        music = serializers.save()
        return Response(f'{music.title} добвлено.')
    

    def get(self, request, id=None):
        if id:
            music = Music.objects.get(pk=id)
            serializers = MusicSerializer(music)
            return Response(serializers.data)
        musics = Music.objects.all()
        serializers = MusicSerializer(musics, many=True)
        return Response(serializers.data)
        

    def put(self, request, id):
        music = Music.object.get(pk=id)
        serializers = MusicSerializer(music, data = request.data)
        if serializers.is_valid():
            music = serializers.save()
            return Response({
                'data': serializers.data, 
                'message': f'{music.title} изменено.'
                })
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        music = Music.object.get(pk=id)
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class PlayListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PlayListSerializer(data=request.data)
        if serializer.is_valid():
            list = serializer.save()
            return Response({
                'data':serializer.data,
                'message':f'Плейлисть {list.title} добавленю'
            })
        
    def get(self, request):
        list = PlayList.objects.all()
        serializer = PlayListSerializer(list, many=True)
        return Response(serializer.data)
    
    def put(self, request, id):
        list = PlayList.object.get(pk=id)
        serializer = PlayListSerializer(list, data=request.data)
        if serializer.is_valid():
            list = serializer.save()
            return Response({
                'data':serializer.data,
                'message':f'Плейлисть {list.title} изменен.'
            })
    
    def delete(self, request, id):
        list = PlayList.object.get(pk=id)
        list.delete()
        return Response(f'Плейлисть Уничтожен!', status=status.HTTP_204_NO_CONTENT)