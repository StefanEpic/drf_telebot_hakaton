import requests
from aiogram import types

from telebot_config import SITE_URL
from .utils.keyboards import vote_emotion_keyboard, vote_food_keyboard, select_video_keyboard


async def start(message: types.Message) -> None:
    await message.reply(
        f"👋 Привет, {message.from_user.first_name}!\n Это бот Приятного Ильдара!",
    )


async def vote_emotion(message: types.Message) -> None:
    """
    Создание голосования видео - эмоция
    """
    get_video_url = f"{SITE_URL}/api/v1/vote/random"
    response = requests.get(get_video_url)
    video_url = response.json()["url"]
    video_id = response.json()["id"]

    get_emotions_url = f"{SITE_URL}/api/v1/emotions"
    response = requests.get(get_emotions_url)
    emotions_list = response.json()
    await message.reply(text=f"{video_url}", reply_markup=await vote_emotion_keyboard(emotions_list, video_id))


async def vote_food(message: types.Message) -> None:
    """
    Создание голосования видео - закуска
    """
    get_video_url = f"{SITE_URL}/api/v1/vote/random"
    response = requests.get(get_video_url)
    video_url = response.json()["url"]
    video_id = response.json()["id"]

    get_food_url = f"{SITE_URL}/api/v1/foods"
    response = requests.get(get_food_url)
    food_list = response.json()

    await message.reply(f"{video_url}", reply_markup=await vote_food_keyboard(food_list, video_id))


async def select_video(message: types.Message) -> None:
    """
    Подбор видео по эмоции
    """
    get_emotions_url = f"{SITE_URL}/api/v1/emotions"
    response = requests.get(get_emotions_url)
    emotions_list = response.json()
    await message.reply("Выберите эмоцию для подбора видео 🤔",
                        reply_markup=await select_video_keyboard(emotions_list)
                        )
