from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_info_type = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="Учителям", callback_data='teacher'),
                                        InlineKeyboardButton(text="Ученикам", callback_data='student')
                                    ],
                                    [
                                        InlineKeyboardButton(text="Кураторым", callback_data='curator'),
                                        InlineKeyboardButton(text="Завучям", callback_data='head_teacher')
                                    ],
                                    [
                                        InlineKeyboardButton(text="Тех-персонад", callback_data='tech_worker'),
                                        InlineKeyboardButton(text="text", callback_data='text')
                                    ]
                                ])