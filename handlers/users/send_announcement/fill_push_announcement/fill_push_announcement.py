from loader import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp

from states import fill_Ad_Event

from .configF import chat_id

from utils.db_api import quick_commands as commands

#fill Ad Event____________________________________________________________________________________

@dp.callback_query_handler(text='fill_announcement')
async def send_announcement(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer("Отправьте афишу мероприятия.")
    await fill_Ad_Event.photo.set()

@dp.message_handler(content_types=['photo'], state=fill_Ad_Event.photo)
async def state1(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[0].file_id)
    await message.answer(f'Укажите дату мероприятия или утраты вещи. ')
    await fill_Ad_Event.next()

@dp.message_handler(state=fill_Ad_Event.date_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(date_event=answer)
    await message.answer(f'Укажите време провидения ивента')
    await fill_Ad_Event.next()

@dp.message_handler(state=fill_Ad_Event.time_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(time_event=answer)
    await message.answer(f'Укажите описания ивента')
    await fill_Ad_Event.next()

@dp.message_handler(state=fill_Ad_Event.description_event)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(description_event=answer)
    data = await state.get_data()
    photo = data.get('photo')
    date_event = data.get('date_event')
    time_event = data.get('time_event')
    description_event = data.get('description_event')
    print(chat_id)
    for id in chat_id:
        async with state.proxy() as data:
            await bot.send_photo(chat_id=id, photo=photo, caption=f'*{date_event}*'
                                                                  f'\n\n'
                                                                  f'_{time_event}_'
                                                                  f'\n\n'
                                                                  f'{description_event}', parse_mode="Markdown")
        chat_id.remove(id)
    await commands.add_Fill_Ad_Event(photo=photo,
                                     date_event=date_event,
                                     time_event=time_event,
                                     description_event=description_event)
    await state.finish()



