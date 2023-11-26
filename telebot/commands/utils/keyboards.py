from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..utils.callback_factory import EmotionVideo, FoodVideo, SelectVideo


async def vote_emotion_keyboard(list_buttons: dict, video_id: int) -> InlineKeyboardMarkup:
    """
    Создание клавиатуры эмоций
    """
    keyboard_builder = InlineKeyboardBuilder()
    for button in list_buttons:
        keyboard_builder.button(
            text=f"{button['title']}",
            callback_data=EmotionVideo(emotion_id=button["id"], video_id=video_id),
        )

    keyboard_builder.adjust(1, 2)
    return keyboard_builder.as_markup()


async def vote_food_keyboard(list_buttons: dict, video_id: int) -> InlineKeyboardMarkup:
    """
    Создание клавиатуры закусок
    """
    keyboard_builder = InlineKeyboardBuilder()
    for button in list_buttons:
        keyboard_builder.button(
            text=f"{button['title']}",
            callback_data=FoodVideo(food_id=button["id"], video_id=video_id),
        )

    keyboard_builder.adjust(1, 2)
    return keyboard_builder.as_markup()


async def select_video_keyboard(list_buttons: dict) -> InlineKeyboardMarkup:
    """
    Создание клавиатуры подбора видео по эмоции
    """
    keyboard_builder = InlineKeyboardBuilder()
    for button in list_buttons:
        keyboard_builder.button(
            text=f"{button['title']}",
            callback_data=SelectVideo(emotion_id=button["id"]),
        )

    keyboard_builder.adjust(1, 2)
    return keyboard_builder.as_markup()
