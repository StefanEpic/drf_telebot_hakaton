import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from telebot_config import BOT_TOKEN
from commands.base import start_bot
from commands.callbacks import send_emotion_video_result, send_food_video_result, get_selected_video
from commands.commands import start, vote_emotion, vote_food, select_video
from commands.utils.callback_factory import EmotionVideo, FoodVideo, SelectVideo


async def main() -> None:
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.startup.register(start_bot)
    dp.message.register(start, Command(commands="start"))
    dp.message.register(vote_emotion, Command(commands="vote_emotion"))
    dp.message.register(vote_food, Command(commands="vote_food"))
    dp.message.register(select_video, Command(commands="select_video"))

    dp.callback_query.register(send_emotion_video_result, EmotionVideo.filter())
    dp.callback_query.register(send_food_video_result, FoodVideo.filter())
    dp.callback_query.register(get_selected_video, SelectVideo.filter())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
