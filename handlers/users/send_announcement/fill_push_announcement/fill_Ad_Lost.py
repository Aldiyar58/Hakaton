from loader import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp

from states import fill_Ad_Lost

from .configF import chat_id
#fill Ad Last________________________________________________________________________________

@dp.callback_query_handler(text='fill_Ad_Lost')
async def send_Ad_Lost(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer("Отправьте фото утерянной вещи.")
    await fill_Ad_Lost.photo.set()

@dp.message_handler(content_types=['photo'], state=fill_Ad_Lost.photo)
async def state1(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[0].file_id)
    await message.answer(f'Укажите дату утраты вещи.')
    await fill_Ad_Lost.next()

@dp.message_handler(state=fill_Ad_Lost.date_lost)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(date_lost=answer)
    await message.answer(f'Укажите описания потереной вещи')
    await fill_Ad_Lost.next()

@dp.message_handler(state=fill_Ad_Lost.description_item)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(description_item=answer)
    data = await state.get_data()
    photo = data.get('photo')
    date_event = data.get('date_lost')
    description_event = data.get('description_item')
    print(chat_id)
    for id in chat_id:
        async with state.proxy() as data:
            await bot.send_photo(chat_id=id, photo=photo, caption=f'*{date_event}*'
                                                                  f'\n\n'
                                                                  f'{description_event}', parse_mode="Markdown")
        chat_id.remove(id)
    await state.finish()
