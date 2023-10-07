from aiogram.dispatcher.filters.state import StatesGroup, State

class loginInSUH(StatesGroup):
    loginIINorEmail = State()
    password = State()