import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Импортируем функции из нашего файла database.py
from database import init_db, add_note, get_notes

TOKEN = "8843075637:AAGs06wqwP-QaczRXq4xcUORjd1fWdhaXT8"

bot = Bot(token=TOKEN)
dp = Dispatcher()


# 1. Шаг для FSM: Создаем группу состояний
class Form(StatesGroup):
    waiting_for_note_text = State()  # Состояние ожидания текста заметки


# Функция для создания главного меню (кнопок на клавиатуре)
def get_main_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="📝 Добавить заметку")
    builder.button(text="🗂 Мои заметки")
    # Размещаем кнопки в один столбец (по 1 в ряд)
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Это твой личный бот для заметок.",
        reply_markup=get_main_keyboard()
    )


# Обработчик кнопки "📝 Добавить заметку"
@dp.message(lambda message: message.text == "📝 Добавить заметку")
async def create_note_start(message: types.Message, state: FSMContext):
    await message.answer("Введите текст вашей заметки:")
    # Переводим пользователя в состояние ожидания текста
    await state.set_state(Form.waiting_for_note_text)


# Обработчик текста, когда бот находится в состоянии waiting_for_note_text
@dp.message(Form.waiting_for_note_text)
async def create_note_finish(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    note_text = message.text

    # Сохраняем заметку в базу данных
    add_note(user_id, note_text)

    await message.answer("✅ Заметка успешно сохранена!", reply_markup=get_main_keyboard())
    # Сбрасываем состояние (выходим из режима ожидания), чтобы бот снова реагировал на обычные команды
    await state.clear()


# Обработчик кнопки "🗂 Мои заметки"
@dp.message(lambda message: message.text == "🗂 Мои заметки")
async def show_notes(message: types.Message):
    user_id = message.from_user.id
    # Получаем список заметок из базы данных
    notes = get_notes(user_id)

    if not notes:
        await message.answer("У вас пока нет сохраненных заметок.")
        return

    response = "<b>Ваши заметки:</b>\n\n"
    for idx, (note_id, text) in enumerate(notes, 1):
        response += f"{idx}. {text}\n"

    # parse_mode="HTML" позволяет использовать теги <b> для жирного текста
    await message.answer(response, parse_mode="HTML")


async def main():
    # Инициализируем базу данных (создаем таблицу, если её нет)
    init_db()
    print("База данных запущена.")
    print("Бот успешно запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())