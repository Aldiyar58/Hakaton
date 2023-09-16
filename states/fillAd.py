from aiogram.dispatcher.filters.state import StatesGroup, State


class fill_Ad_Event(StatesGroup):
    photo = State()
    date_event = State()
    time_event = State()
    description_event = State()

class fill_Ad_Lost(StatesGroup):
    photo = State()
    date_lost = State()
    description_item = State()

class event_without_photo(StatesGroup):
    date_event = State()
    time_event = State()
    description_event = State()

class fill_Ad_news(StatesGroup):
    text= State()

