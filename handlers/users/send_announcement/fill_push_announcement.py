from loader import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp

from states import fill_ad

chat_id = []

@dp.callback_query_handler(text='fill_announcement')
async def send_announcement(callback: types.CallbackQuery):
    await callback.message.answer('text')
    await callback.answer()
    await callback.message.answer("Отправьте фото утерянной вещи или афишу мероприятия.")
    await fill_ad.photo.set()

@dp.message_handler(content_types=['photo'], state=fill_ad.photo)
async def state1(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[0].file_id)
    await message.answer(f'Укажите дату мероприятия или утраты вещи. ')
    await fill_ad.next()

@dp.message_handler(state=fill_ad.date_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(date_event=answer)
    await message.answer(f'Укажите време провидения ивента')
    await fill_ad.next()

@dp.message_handler(state=fill_ad.time_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(time_event=answer)
    await message.answer(f'Укажите описания ивента')
    await fill_ad.next()

@dp.message_handler(state=fill_ad.description_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(description_event=answer)
    # data = await state.get_data()
    # photo = data.get('photo')
    # date_event = data.get('date_event')
    # time_event = data.get('time_event')
    # description_event = data.get('description_event')
    for id in chat_id:
        async with state.proxy() as data:
            await bot.send_message(chat_id=id, text=str(data))
        chat_id.remove(id)
    await state.finish()
