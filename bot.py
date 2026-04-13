import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup


BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Старт")]],
    resize_keyboard=True,
)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        "Привет! Нажми кнопку Старт, чтобы начать.",
        reply_markup=start_keyboard,
    )


@dp.message(F.text == "Старт")
async def start_button_handler(message: Message) -> None:
    await message.answer("Отлично, запуск выполнен. Чем могу помочь?")


@dp.message(F.text)
async def echo_handler(message: Message) -> None:
    await message.answer(f"Ты написал: {message.text}")


async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
