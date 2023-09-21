from sqlalchemy import Column, BigInteger, String, sql, Text

from utils.db_api.db_gino import TimedBaseModel

class Fill_Ad_Event(TimedBaseModel):
    __tablename__ = 'fill_Ad_Event'
    photo = Column(Text)
    date_event = Column(String(200))
    time_event = Column(String(50))
    description_event = Column(String(3000))
    query: sql.select


class Fill_Ad_Lost(TimedBaseModel):
    __tablename__ = 'fill_Ad_Lost'
    photo = Column(Text)
    date_lost = Column(String(200))
    description_item = Column(String(3000))
    query: sql.select


class Event_without_photo(TimedBaseModel):
    __tablename__ = 'event_without_photo'
    date_event = Column(String(200))
    time_event = Column(String(50))
    description_event = Column(String(3000))
    query: sql.select


class Fill_Ad_news(TimedBaseModel):
    __tablename__ = 'fill_Ad_news'
    news_text = Column(String(3000))
    query: sql.select


