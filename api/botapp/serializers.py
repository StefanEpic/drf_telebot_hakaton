from typing import Union, Any
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Video, Emotion, Food, VideoEmotion, VideoFood


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ["id", "title", "sticker_id"]


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ["id", "title", "sticker_id"]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["id", "title", "url"]


class VideoDetailSerializer(serializers.ModelSerializer):
    emotion = serializers.SerializerMethodField()
    food = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ["id", "title", "url", "emotion", "food"]

    @extend_schema_field(EmotionSerializer)
    def get_emotion(self, obj: Emotion) -> Union[EmotionSerializer, None]:
        """
        Вернуть самую популярную эмоцию этого видео
        """
        video_emotions = obj.videoemotion_set.all()
        if video_emotions:
            max_count_emotion = video_emotions.order_by("-count").first()
            return EmotionSerializer(max_count_emotion.emotion).data
        return None

    @extend_schema_field(FoodSerializer)
    def get_food(self, obj: Food) -> Union[FoodSerializer, None]:
        """
        Вернуть самую популярную закуску этого видео
        """
        video_foods = obj.videofood_set.all()
        if video_foods:
            max_count_food = video_foods.order_by("-count").first()
            return FoodSerializer(max_count_food.food).data
        return None


class EmotionDetailSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()

    class Meta:
        model = Emotion
        fields = ["id", "title", "sticker_id", "video"]

    @extend_schema_field(VideoSerializer)
    def get_video(self, obj: Video) -> Union[VideoSerializer, None]:
        """
        Вернуть самое популярное видео этой эмоции
        """
        emotion_videos = obj.videoemotion_set.all()
        if emotion_videos:
            max_count_video = emotion_videos.order_by("-count").first()
            return VideoSerializer(max_count_video.video).data
        return None


class FoodDetailSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = ["id", "title", "sticker_id", "video"]

    @extend_schema_field(VideoSerializer)
    def get_video(self, obj: Video) -> Union[VideoSerializer, None]:
        """
        Вернуть самое популярное видео этой зкуски
        """
        food_videos = obj.videofood_set.all()
        if food_videos:
            max_count_video = food_videos.order_by("-count").first()
            return VideoSerializer(max_count_video.video).data
        return None


class VideoEmotionSerializer(serializers.Serializer):
    """
    Сохранение результата голосования видео - эмоция
    """

    video_id = serializers.IntegerField()
    emotion_id = serializers.IntegerField()

    def create(self, validated_data: dict[str, Any]) -> VideoEmotion:
        video_id = validated_data.pop("video_id")
        emotion_id = validated_data.pop("emotion_id")

        video = Video.objects.filter(id=video_id).first()
        emotion = Emotion.objects.filter(id=emotion_id).first()

        if video is None:
            raise ValidationError("Video not found")
        if emotion is None:
            raise ValidationError("Emotion not found")

        video_emotion = VideoEmotion.objects.filter(video=video, emotion=emotion).first()
        if video_emotion is None:
            video_emotion = VideoEmotion(video=video, emotion=emotion)
        video_emotion.increment_count()
        video_emotion.save()
        return video_emotion


class VideoFoodSerializer(serializers.Serializer):
    """
    Сохранение результата голосования видео - закуска
    """

    video_id = serializers.IntegerField()
    food_id = serializers.IntegerField()

    def create(self, validated_data: dict[str, Any]) -> VideoFood:
        video_id = validated_data.pop("video_id")
        food_id = validated_data.pop("food_id")

        video = Video.objects.filter(id=video_id).first()
        food = Food.objects.filter(id=food_id).first()

        if video is None:
            raise ValidationError("Video not found")
        if food is None:
            raise ValidationError("Food not found")

        video_food = VideoFood.objects.filter(video=video, food=food).first()
        if video_food is None:
            video_food = VideoFood(video=video, food=food)
        video_food.increment_count()
        video_food.save()
        return video_food
