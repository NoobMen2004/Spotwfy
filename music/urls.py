from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MusicViewSet, PlayListViewSet

router = DefaultRouter()
router.register(r'cat', CategoryViewSet, basename='cat')
router.register(r'music', MusicViewSet, basename='music')
router.register(r'playlist', PlayListViewSet, basename='playlist')

urlpatterns = router.urls
