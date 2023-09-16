from loader import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp

from states import event_without_photo

from .configF import chat_id

#without photo_____________________________________________________________________________

@dp.callback_query_handler(text='event_without_photo')
async def send_announcement(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer(f'Укажите дату мероприятия или утраты вещи.')
    await event_without_photo.date_event.set()

@dp.message_handler(state=event_without_photo.date_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(date_event=answer)
    await message.answer(f'Укажите време провидения ивента')
    await event_without_photo.next()

@dp.message_handler(state=event_without_photo.time_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(time_event=answer)
    await message.answer(f'Укажите описания ивента')
    await event_without_photo.next()

@dp.message_handler(state=event_without_photo.description_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(description_event=answer)
    data = await state.get_data()
    date_event = data.get('date_event')
    time_event = data.get('time_event')
    description_event = data.get('description_event')
    print(chat_id)
    for id in chat_id:
        async with state.proxy() as data:
            await bot.send_message(chat_id=id, text=f'*{date_event}*'
                                                    f'\n\n'
                                                    f'_{time_event}_'
                                                    f'\n\n'
                                                    f'{description_event}', parse_mode="Markdown")
        chat_id.remove(id)
    await state.finish()
