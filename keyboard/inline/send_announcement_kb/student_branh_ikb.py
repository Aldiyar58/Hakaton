from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_students = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='Классы', callback_data='grade'),
                                              InlineKeyboardButton(text='Шаныраки', callback_data='shanrak')

                                          ]
                                      ])

ikb_grade_list = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='7 class', callback_data='7_grade'),
                                              InlineKeyboardButton(text='8 class', callback_data='8_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='9 class', callback_data='9_grade'),
                                              InlineKeyboardButton(text='10 class', callback_data='10_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='11 class', callback_data='11_grade'),
                                              InlineKeyboardButton(text='12 class', callback_data='12_grade'),
                                              InlineKeyboardButton(text='all class', callback_data='all_grade')

                                          ]
                                      ])

ikb_7_grade_list = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='7 A', callback_data='7_A_grade'),
                                              InlineKeyboardButton(text='7 B', callback_data='7_B_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='7 C', callback_data='7_C_grade'),
                                              InlineKeyboardButton(text='7 D', callback_data='7_D_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='7 E', callback_data='7_E_grade'),
                                              InlineKeyboardButton(text='7 F', callback_data='7_F_grade'),
                                              InlineKeyboardButton(text='all class', callback_data='all_7_grade')

                                          ]
                                      ])

ikb_8_grade_list = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='8 A', callback_data='8_A_grade'),
                                              InlineKeyboardButton(text='8 B', callback_data='8_B_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='8 C', callback_data='8_C_grade'),
                                              InlineKeyboardButton(text='8 D', callback_data='8_D_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='8 E', callback_data='8_E_grade'),
                                              InlineKeyboardButton(text='8 F', callback_data='8_F_grade'),
                                              InlineKeyboardButton(text='all class', callback_data='all_8_grade')

                                          ]
                                      ])

ikb_9_grade_list = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='9 A', callback_data='9_A_grade'),
                                              InlineKeyboardButton(text='9 B', callback_data='9_B_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='9 C', callback_data='9_C_grade'),
                                              InlineKeyboardButton(text='9 D', callback_data='9_D_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='9 E', callback_data='9_E_grade'),
                                              InlineKeyboardButton(text='9 F', callback_data='9_F_grade'),
                                              InlineKeyboardButton(text='all class', callback_data='all_9_grade')

                                          ]
                                      ])

ikb_10_grade_list = InlineKeyboardMarkup(row_width=2,
                                         inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='10 A', callback_data='10_A_grade'),
                                              InlineKeyboardButton(text='10 B', callback_data='10_B_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='10 C', callback_data='10_C_grade'),
                                              InlineKeyboardButton(text='10 D', callback_data='10_D_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='10 E', callback_data='10_E_grade'),
                                              InlineKeyboardButton(text='10 F', callback_data='10_F_grade'),
                                              InlineKeyboardButton(text='all class', callback_data='all_10_grade')

                                          ]
                                      ])

ikb_11_grade_list = InlineKeyboardMarkup(row_width=2,
                                         inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='11 A', callback_data='11_A_grade'),
                                              InlineKeyboardButton(text='11 B', callback_data='11_B_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='11 C', callback_data='11_C_grade'),
                                              InlineKeyboardButton(text='11 D', callback_data='11_D_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='11 E', callback_data='11_E_grade'),
                                              InlineKeyboardButton(text='11 F', callback_data='11_F_grade'),
                                              InlineKeyboardButton(text='all class', callback_data='all_11_grade')

                                          ]
                                      ])

ikb_12_grade_list = InlineKeyboardMarkup(row_width=2,
                                         inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='12 A', callback_data='7_grade'),
                                              InlineKeyboardButton(text='12 B', callback_data='8_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='12 C', callback_data='9_grade'),
                                              InlineKeyboardButton(text='12 D', callback_data='10_grade')

                                          ],
                                          [
                                              InlineKeyboardButton(text='12 E', callback_data='11_grade'),
                                              InlineKeyboardButton(text='12 F', callback_data='12_grade'),
                                              InlineKeyboardButton(text='all class', callback_data='all_12_grade')

                                          ]
                                      ])