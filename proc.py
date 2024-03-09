from quiz import quiz_d
import asyncio
import logging
import database as db
from database import create_table
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import F
#import nest_asyncio
#nest_asyncio.apply()
logging.basicConfig(level=logging.INFO)

API_TOKEN = '6273033030:AAEJv4OF_fLWTb6BmhsFr6-Gt-u87uAMfNI'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
quiz_data=quiz_d()
def generate_options_keyboard(answer_options, right_answer):
    builder = InlineKeyboardBuilder()

    for option in answer_options:
        builder.add(types.InlineKeyboardButton(
            text=option,
            callback_data=str(option))
            #"right_answer" if option == right_answer else "wrong_answer")

        )
        #print(option)
    builder.adjust(1)
    return builder.as_markup()


@dp.callback_query()
async def right_answer(callback: types.CallbackQuery):

    await callback.bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )
    #print("callback.message:   ", callback.message)
    #print("callback ", callback)
    #print("callback.data:   ", callback.data)
    #print("callback.message.callback_data: ", callback.chat.callback_data)
    #print("Ответ  ", F.text)
    await callback.message.answer(f"Твой ответ: {callback.data}")
    #await callback.message.answer(callback.message.message_id)
    current_question_index = await db.get_quiz_index(callback.from_user.id)
    #print("Индекс вопроса ", current_question_index)
    correct_index = quiz_data[current_question_index]['correct_option']
    opts = quiz_data[current_question_index]['options']
    #print("Правильный ответ  ", opts[correct_index])
    if callback.data == opts[correct_index]:
        await callback.message.answer("Правильно!")
        current_top = await db.get_top_index(callback.from_user.id)
        # Обновление номера текущего вопроса в базе данных
        current_top += 1
        current_question_index += 1
        await db.update_quiz_index(callback.from_user.id, current_question_index)
        await db.update_top_index(callback.from_user.id, current_top, callback.from_user.first_name)
    else:
        correct_option = quiz_data[current_question_index]['correct_option']
        await callback.message.answer(f"Неправильно. Правильный ответ:    {quiz_data[current_question_index]['options'][correct_option]}")
        current_question_index += 1
        await db.update_quiz_index(callback.from_user.id, current_question_index)

    if current_question_index < len(quiz_data):
        await get_question(callback.message, callback.from_user.id)
    else:
        await callback.message.answer("Это был последний вопрос. Квиз завершен!")
        s = await db.get_top_score()
        print(str(s))
        await callback.message.answer(f"Топ 5 игроков  { str(s)}")


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Начать игру"))
    await message.answer("Добро пожаловать в квиз!", reply_markup=builder.as_markup(resize_keyboard=True))

@dp.message(F.text=="Начать игру")
@dp.message(Command("quiz"))
async def cmd_quiz(message: types.Message):

    await message.answer(f"Давайте начнем квиз!")
    await new_quiz(message)
async def get_question(message, user_id):

    # Получение текущего вопроса из словаря состояний пользователя
    current_question_index = await db.get_quiz_index(user_id)
    correct_index = quiz_data[current_question_index]['correct_option']
    opts = quiz_data[current_question_index]['options']
    kb = generate_options_keyboard(opts, opts[correct_index])
    await message.answer(f"{quiz_data[current_question_index]['question']}", reply_markup=kb)


async def new_quiz(message):
    user_id = message.from_user.id
    current_question_index = 0
    await db.update_quiz_index(user_id, current_question_index)
    await get_question(message, user_id)
    
async def main():

    # Запускаем создание таблицы базы данных
    await create_table()
    #await delete_table
    #await alter_table()
    await dp.start_polling(bot)