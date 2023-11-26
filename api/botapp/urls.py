from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    VideoViewset,
    EmotionViewset,
    FoodViewset,
    VideoEmotionView,
    VideoFoodView,
    VideoDetailView,
    EmotionDetailView,
    FoodDetailView,
    VideoRandomView,
)

router = DefaultRouter()
router.register(r"videos", VideoViewset, basename="videos")
router.register(r"videos", VideoDetailView, basename="video_detail")
router.register(r"emotions", EmotionViewset, basename="emotions")
router.register(r"emotions", EmotionDetailView, basename="emotion_detail")
router.register(r"foods", FoodViewset, basename="foods")
router.register(r"foods", FoodDetailView, basename="food_detail")

urlpatterns = [
    path("", include(router.urls)),
    path("vote/emotion/", VideoEmotionView.as_view(), name="vote_emotion"),
    path("vote/food/", VideoFoodView.as_view(), name="vote_food"),
    path("vote/random/", VideoRandomView.as_view(), name="vote_random"),
]
