from random import randint

from rest_framework import generics, viewsets
from rest_framework import mixins
from rest_framework.request import Request
from rest_framework.response import Response

from .docs import (
    video_summary,
    video_detail_summary,
    emotion_summary,
    food_summary,
    emotion_detail_summary,
    food_detail_summary,
    video_emotion_summary,
    video_food_summary,
    video_random_summary,
)
from .models import Video, Emotion, Food
from .serializers import (
    VideoSerializer,
    EmotionSerializer,
    FoodSerializer,
    VideoDetailSerializer,
    VideoEmotionSerializer,
    VideoFoodSerializer,
    EmotionDetailSerializer,
    FoodDetailSerializer,
)


@video_summary
class VideoViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Video.objects.all().order_by("id")
    serializer_class = VideoSerializer


@emotion_summary
class EmotionViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Emotion.objects.all().order_by("id")
    serializer_class = EmotionSerializer


@food_summary
class FoodViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Food.objects.all().order_by("id")
    serializer_class = FoodSerializer


@video_detail_summary
class VideoDetailView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializer


@emotion_detail_summary
class EmotionDetailView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Emotion.objects.all()
    serializer_class = EmotionDetailSerializer


@food_detail_summary
class FoodDetailView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodDetailSerializer


@video_emotion_summary
class VideoEmotionView(generics.CreateAPIView):
    serializer_class = VideoEmotionSerializer


@video_food_summary
class VideoFoodView(generics.CreateAPIView):
    serializer_class = VideoFoodSerializer


@video_random_summary
class VideoRandomView(generics.RetrieveAPIView):
    serializer_class = VideoSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        """
        Получить рандомное видео
        """
        videos = Video.objects.all()
        index = randint(0, len(videos) - 1)
        random_video = videos[index]
        return Response(VideoSerializer(random_video).data)
