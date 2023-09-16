from loader import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp

from states import fill_Ad_news

from .configF import chat_id

#fill Ad News___________________________________________________________________

@dp.callback_query_handler(text='fill_Ad_news')
async def send_announcement(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer(f'Укажите дату мероприятия или утраты вещи.')
    await fill_Ad_news.text.set()


@dp.message_handler(state=fill_Ad_news.text)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(text=answer)
    data = await state.get_data()
    text = data.get('text')
    print(chat_id)
    for id in chat_id:
        async with state.proxy() as data:
            await bot.send_message(chat_id=id, text=f'{text}', parse_mode="Markdown")
        chat_id.remove(id)
    await state.finish()
