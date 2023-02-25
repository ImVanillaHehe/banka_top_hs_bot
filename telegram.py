import asyncio
import json
import os
import time
from aiogram.utils.markdown import hbold
from aiogram import Bot, Dispatcher, executor, types
from parse import mainstream
import dotenv

dotenv.load_dotenv(".env")
bot = Bot(token=os.getenv("TOKEN"), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("привет, я бот банки, пока доступна только команда /ranks")


@dp.message_handler(commands="ranks")
async def start(message: types.Message):
    button = types.InlineKeyboardButton('Ранги банки', callback_data='ranks')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button)

    await message.answer("Нажми на кнопку чтобы увидеть топ Банки", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == 'ranks')
async def process_callback_ranks(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer("Запрос обрабатывается. Примерное время ожидания 2-3 минуты. Не нажимай на кнопку "
                                        "пока не выведет список игроков. Просто подожди 2-3 минуты, сука ")
    time.sleep(2)
    await callback_query.message.answer("Если кого нет в списке, просто нажми заново на кнопку")

    try:
        await asyncio.wait_for(mainstream(1, 4000) )
    except KeyError:
        await callback_query.message.answer("Что-то пошло не так. Попробуй еще раз")
        await callback_query.message.answer("Бот умер")

    with open("banka player_list.json", "r") as file:
        data = json.load(file)

        for item in data:
            card = f"{hbold('Ник: ')} {item.get('account_name')}\n" \
                   f"{hbold('Рейтинг: ')} {item.get('rating')}\n" \
                   f"{hbold('Ранг в таблице лидеров: ')} {item.get('rank')}"
            await callback_query.message.answer(card)
            time.sleep(1)


if __name__ == "__main__":
    executor.start_polling(dp)
