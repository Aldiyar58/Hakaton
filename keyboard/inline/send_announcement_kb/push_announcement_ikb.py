from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_push_announcement = InlineKeyboardMarkup(row_width=2,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(text='Заполнить обявление', callback_data='fill_announcement'),
                                                     InlineKeyboardButton(text='Отмена', callback_data='aaaa')
                                                 ]
                                             ])