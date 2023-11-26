from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot) -> None:
    """
    Описание команд
    """
    commands = [
        BotCommand(command="vote_emotion", description="Проголосовать: Какая эмоция ассоциируется с видео"),
        BotCommand(command="vote_food", description="Проголосовать: Какая закуска ассоциируется с видео"),
        BotCommand(command="select_video", description="Подобрать видео по эмоции"),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def start_bot(bot: Bot) -> None:
    await set_commands(bot)
