from aiogram.filters.callback_data import CallbackData


class EmotionVideo(CallbackData, prefix="emotion"):
    emotion_id: int
    video_id: int


class FoodVideo(CallbackData, prefix="food"):
    food_id: int
    video_id: int


class SelectVideo(CallbackData, prefix="video"):
    emotion_id: int
