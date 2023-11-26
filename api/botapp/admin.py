from django.contrib import admin
from .models import (
    Video,
    Emotion,
    Food,
    VideoEmotion,
    VideoFood,
)


class VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url")
    list_display_links = ("title",)
    search_fields = (
        "title",
        "id",
    )
    list_per_page = 20
    ordering = ["-id"]
    fieldsets = [
        ("Видео", {"fields": ["title", "url"]}),
    ]


class EmotionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "sticker_id")
    list_display_links = ("title",)
    search_fields = (
        "title",
        "id",
    )
    list_per_page = 20
    ordering = ["-id"]
    fieldsets = [
        ("Эмоция", {"fields": ["title", "sticker_id"]}),
    ]


class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "sticker_id")
    list_display_links = ("title",)
    search_fields = (
        "title",
        "id",
    )
    list_per_page = 20
    ordering = ["-id"]
    fieldsets = [
        ("Закуска", {"fields": ["title", "sticker_id"]}),
    ]


class VideoEmotionAdmin(admin.ModelAdmin):
    list_display = ("id", "video", "emotion", "count")
    list_display_links = ("video",)
    search_fields = (
        "video",
        "emotion",
        "id",
    )
    list_per_page = 20
    ordering = ["-id"]


class FoodEmotionAdmin(admin.ModelAdmin):
    list_display = ("id", "video", "food", "count")
    list_display_links = ("video",)
    search_fields = (
        "video",
        "food",
        "id",
    )
    list_per_page = 20
    ordering = ["-id"]


admin.site.register(Video, VideoAdmin)
admin.site.register(Emotion, EmotionAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(VideoEmotion, VideoEmotionAdmin)
admin.site.register(VideoFood, FoodEmotionAdmin)
