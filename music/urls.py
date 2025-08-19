from django.urls import path
from .views import *

urlpatterns = [
    path('cat/', CategoryAPIView.as_view()),
    path('music/', MusicAPIView.as_view()),
    path('PlayList/', PlayListAPIView.as_view()),
]