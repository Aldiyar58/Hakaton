from loader import bot, dp
from aiogram import types
from keyboard.inline import ikb_info_type, ikb_students, ikb_grade_list, ikb_7_grade_list, ikb_8_grade_list, ikb_9_grade_list, ikb_10_grade_list, ikb_11_grade_list, ikb_12_grade_list, ikb_push_announcement
from .fill_push_announcement import chat_id

@dp.message_handler(commands=['Отправит_обявление'])
async def command_start(message: types.Message):
    await message.answer(f"hi chose where we send news \n"
                         f"text text text text text\n"
                         f"text text text text text", reply_markup=ikb_info_type)

@dp.callback_query_handler(text='student')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_students)
    await callback.answer()

@dp.callback_query_handler(text='grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_grade_list)
    await callback.answer()

@dp.callback_query_handler(text='7_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_7_grade_list)
    await callback.answer()

#--------------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text='7_A_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='7_B_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='7_C_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='7_D_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='7_E_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='7_F_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='all_7_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

#--------------------------------------------------------------------------------------------------------------------







@dp.callback_query_handler(text='8_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_8_grade_list)
    await callback.answer()
#--------------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text='8_A_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()
    chat_id.append('-988474178')

@dp.callback_query_handler(text='8_B_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()
    chat_id.append('-949717011')

@dp.callback_query_handler(text='8_C_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()
    chat_id.append('-941669612')

@dp.callback_query_handler(text='8_D_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()
    chat_id.append('')

@dp.callback_query_handler(text='8_E_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()
    chat_id.append('-941669612')

@dp.callback_query_handler(text='8_F_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()
    chat_id.append('-941669612')

@dp.callback_query_handler(text='all_8_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()
    chat_id.append('-941669612')

#--------------------------------------------------------------------------------------------------------------------






@dp.callback_query_handler(text='9_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_9_grade_list)
    await callback.answer()

#--------------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text='9_A_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='9_B_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='9_C_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='9_D_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='9_E_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='9_F_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='all_9_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

#--------------------------------------------------------------------------------------------------------------------





@dp.callback_query_handler(text='10_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_10_grade_list)
    await callback.answer()

#--------------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text='10_A_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='10_B_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='10_C_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='10_D_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='10_E_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='10_F_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='all_10_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

#--------------------------------------------------------------------------------------------------------------------





@dp.callback_query_handler(text='11_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_11_grade_list)
    await callback.answer()

#--------------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text='11_A_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='11_B_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='11_C_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='11_D_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='11_E_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='11_F_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='all_11_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()
#--------------------------------------------------------------------------------------------------------------------






@dp.callback_query_handler(text='12_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_12_grade_list)
    await callback.answer()

#--------------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(text='12_A_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='12_B_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='12_C_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='12_D_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='12_E_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='12_F_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

@dp.callback_query_handler(text='all_12_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

#--------------------------------------------------------------------------------------------------------------------





@dp.callback_query_handler(text='all_grade')
async def command_start(callback: types.CallbackQuery):
    await callback.message.answer('text text text text', reply_markup=ikb_push_announcement)
    await callback.answer()

