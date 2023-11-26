from django.forms import model_to_dict
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from botapp import models
from botapp.models import VideoEmotion, VideoFood


class BaseTestCase(APITestCase):
    def setUp(self) -> None:
        self.emotion = models.Emotion.objects.create(title="Смешное", sticker_id="12345")
        self.emotion2 = models.Emotion.objects.create(title="Грустное", sticker_id="12345")
        self.food = models.Food.objects.create(title="Пицца", sticker_id="12345")
        self.food2 = models.Food.objects.create(title="Бургер", sticker_id="12345")
        self.video = models.Video.objects.create(
            title="Первое видео", url="https://youtu.be/pLoC6PqZz3M?si=WyG_Mtxjaa6JtbW6"
        )
        self.video2 = models.Video.objects.create(
            title="Второе видео", url="https://youtu.be/pLoC6PqZz3M?si=WyG_Mtxjaa6JtbW6"
        )
        video_emotion = VideoEmotion(video=self.video, emotion=self.emotion, count=1)
        video_emotion.save()
        video_food = VideoFood(video=self.video, food=self.food, count=1)
        video_food.save()

        self.emotions_url = reverse("emotions-list")
        self.foods_url = reverse("foods-list")
        self.videos_url = reverse("videos-list")
        self.emotions_detail_url = reverse("emotion_detail-detail", args=(self.emotion.id,))
        self.emotions_detail_url2 = reverse("emotion_detail-detail", args=(self.emotion2.id,))
        self.foods_detail_url = reverse("food_detail-detail", args=(self.food.id,))
        self.foods_detail_url2 = reverse("food_detail-detail", args=(self.food2.id,))
        self.videos_detail_url = reverse("video_detail-detail", args=(self.video.id,))
        self.videos_detail_url2 = reverse("video_detail-detail", args=(self.video2.id,))
        self.vote_emotion_url = reverse("vote_emotion")
        self.vote_food_url = reverse("vote_food")
        self.random_video_url = reverse("vote_random")

    def test_get_emotion_list(self) -> None:
        request = self.client.get(self.emotions_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json()[0], model_to_dict(self.emotion))

    def test_get_food_list(self) -> None:
        request = self.client.get(self.foods_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json()[0], model_to_dict(self.food))

    def test_get_video_list(self) -> None:
        request = self.client.get(self.videos_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json()[0]["title"], self.video.title)
        self.assertEqual(request.json()[0]["url"], self.video.url)

    def test_get_random_video(self) -> None:
        request = self.client.get(self.random_video_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_vote_emotion(self) -> None:
        data = {"video_id": 2, "emotion_id": 2}
        request = self.client.post(self.vote_emotion_url, data=data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(request.json(), data)

        v_e = VideoEmotion.objects.get(video_id=1)
        self.assertEqual(
            str(v_e), f'(ID: {v_e.emotion.id}){v_e.emotion}: (ID: {v_e.video.id})"{v_e.video}" (COUNT: {v_e.count})'
        )

    def test_vote_emotion_video_not_found(self) -> None:
        data = {"video_id": 9999, "emotion_id": 2}
        request = self.client.post(self.vote_emotion_url, data=data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(request.json()[0], "Video not found")

    def test_vote_emotion_emotion_not_found(self) -> None:
        data = {"video_id": 1, "emotion_id": 9999}
        request = self.client.post(self.vote_emotion_url, data=data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(request.json()[0], "Emotion not found")

    def test_vote_food(self) -> None:
        data = {"video_id": 2, "food_id": 2}
        request = self.client.post(self.vote_food_url, data=data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(request.json(), data)

        v_f = VideoFood.objects.get(video_id=1)
        self.assertEqual(
            str(v_f), f'(ID: {v_f.food.id}){v_f.food}: (ID: {v_f.video.id})"{v_f.video}" (COUNT: {v_f.count})'
        )

    def test_vote_food_video_not_found(self) -> None:
        data = {"video_id": 9999, "food_id": 2}
        request = self.client.post(self.vote_food_url, data=data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(request.json()[0], "Video not found")

    def test_vote_food_food_not_found(self) -> None:
        data = {"video_id": 1, "food_id": 9999}
        request = self.client.post(self.vote_food_url, data=data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(request.json()[0], "Food not found")

    def test_get_emotion_detail_with_video(self) -> None:
        request = self.client.get(self.emotions_detail_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json()["title"], self.emotion.title)
        self.assertEqual(request.json()["sticker_id"], self.emotion.sticker_id)
        self.assertEqual(request.json()["video"]["title"], self.video.title)
        self.assertEqual(str(self.emotion), self.emotion.title)

    def test_get_emotion_detail_without_video(self) -> None:
        request = self.client.get(self.emotions_detail_url2)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json()["video"], None)

    def test_get_food_detail_with_video(self) -> None:
        request = self.client.get(self.foods_detail_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json()["title"], self.food.title)
        self.assertEqual(request.json()["sticker_id"], self.food.sticker_id)
        self.assertEqual(request.json()["video"]["title"], self.video.title)
        self.assertEqual(str(self.food), self.food.title)

    def test_get_food_detail_without_video(self) -> None:
        request = self.client.get(self.foods_detail_url2)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json()["video"], None)

    def test_get_video_detail_with_emotion_and_video(self) -> None:
        request = self.client.get(self.videos_detail_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json()["title"], self.video.title)
        self.assertEqual(request.json()["url"], self.video.url)
        self.assertEqual(request.json()["emotion"]["title"], self.emotion.title)
        self.assertEqual(request.json()["food"]["title"], self.food.title)
        self.assertEqual(str(self.video), self.video.title)

    def test_get_video_detail_without_emotion_and_video(self) -> None:
        request = self.client.get(self.videos_detail_url2)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json()["emotion"], None)
        self.assertEqual(request.json()["food"], None)
