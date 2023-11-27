import requests
from aiogram.types import CallbackQuery

from telebot_config import SITE_URL
from .utils.callback_factory import EmotionVideo, FoodVideo, SelectVideo


async def send_emotion_video_result(call: CallbackQuery, callback_data: EmotionVideo) -> None:
    url = f"{SITE_URL}/api/v1/vote/emotion/"
    data = {"video_id": callback_data.video_id, "emotion_id": callback_data.emotion_id}
    response = requests.post(url, data)
    await call.message.delete()
    if response.status_code == 201:
        emotion_url = f"{SITE_URL}/api/v1/emotions/{callback_data.emotion_id}"
        response = requests.get(emotion_url)

        await call.message.answer("Спасибо! Твой голос учтен 🤗")
        await call.message.answer_sticker(f"{response.json()['sticker_id']}")
    else:
        await call.message.answer("Упс, что-то пошло не так 🤪")


async def send_food_video_result(call: CallbackQuery, callback_data: FoodVideo) -> None:
    url = f"{SITE_URL}/api/v1/vote/food/"
    data = {"video_id": callback_data.video_id, "food_id": callback_data.food_id}
    response = requests.post(url, data)
    await call.message.delete()
    if response.status_code == 201:
        food_url = f"{SITE_URL}/api/v1/foods/{callback_data.food_id}"
        response = requests.get(food_url)

        await call.message.answer("Спасибо! Твой голос учтен 🤗")
        await call.message.answer_sticker(f"{response.json()['sticker_id']}")
    else:
        await call.message.answer("Упс, что-то пошло не так 🤪")


async def get_selected_video(call: CallbackQuery, callback_data: SelectVideo) -> None:
    emotion_url = f"{SITE_URL}/api/v1/emotions/{callback_data.emotion_id}"
    video_response = requests.get(emotion_url)

    await call.message.delete()
    if video_response.status_code == 200:
        if video_response.json()["video"]:
            video_url = f'{SITE_URL}/api/v1/videos/{video_response.json()["video"]["id"]}'
            food_response = requests.get(video_url)

            await call.message.answer(f'{video_response.json()["video"]["url"]}')
            if food_response.json()["food"]:
                await call.message.answer("К этому видео отлично подходит закуска:")
                await call.message.answer_sticker(f'{food_response.json()["food"]["sticker_id"]}')
        else:
            await call.message.answer("C этой эмоцией пока не связано ни одно видео 🤪")
    else:
        await call.message.answer("Упс, что-то пошло не так 🤪")
