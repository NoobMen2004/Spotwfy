from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'comments', CommentModelViewSet, basename='comment')
router.register(r'favorites', FavoriteModelViewSet, basename='favorite')
router.register(r'ratings', RatingModelViewSet, basename='ratings')

urlpatterns = router.urls
