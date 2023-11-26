from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Название")
    url = models.URLField(max_length=255, verbose_name="Ссылка на видео")
    emotion = models.ManyToManyField("Emotion", through="VideoEmotion", related_name="video")
    food = models.ManyToManyField("Food", through="VideoFood", related_name="video")

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self) -> str:
        return str(self.title)


class Emotion(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Название")
    sticker_id = models.CharField(max_length=255, verbose_name="ID стикера эмоции")

    class Meta:
        verbose_name = "Эмоция"
        verbose_name_plural = "Эмоции"

    def __str__(self) -> str:
        return str(self.title)


class Food(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Название")
    sticker_id = models.CharField(max_length=255, verbose_name="ID стикера эмоции")

    class Meta:
        verbose_name = "Закуска"
        verbose_name_plural = "Закуски"

    def __str__(self) -> str:
        return str(self.title)


class VideoEmotion(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    count = models.IntegerField(blank=True, default=0)

    class Meta:
        verbose_name = "Связи Видео-эмоции"
        verbose_name_plural = "Связи Видео-эмоции"

        unique_together = ["video", "emotion"]

    def increment_count(self) -> None:
        self.count += 1
        self.save()

    def __str__(self) -> str:
        return f'(ID: {self.emotion.id}){self.emotion}: (ID: {self.video.id})"{self.video}" (COUNT: {self.count})'


class VideoFood(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Связи Видео-закуски"
        verbose_name_plural = "Связи Видео-закуски"

        unique_together = ["video", "food"]

    def increment_count(self) -> None:
        self.count += 1
        self.save()

    def __str__(self) -> str:
        return f'(ID: {self.food.id}){self.food}: (ID: {self.video.id})"{self.video}" (COUNT: {self.count})'
