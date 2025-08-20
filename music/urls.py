from django.urls import path
from .views import *

urlpatterns = [
    path('cat/', CategoryAPIView.as_view()),
    path('cat/<int:id>/', CategoryAPIView.as_view()),
    path('music/', MusicAPIView.as_view()),
    path('music/<int:id>/', MusicAPIView.as_view()),
    path('PlayList/', PlayListAPIView.as_view()),
    path('PlayList/<int:id>/', PlayListAPIView.as_view()),
]