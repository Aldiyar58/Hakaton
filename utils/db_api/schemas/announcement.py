from sqlalchemy import Column, BigInteger, String, sql, Text, ARRAY, Integer

from utils.db_api.db_gino import TimedBaseModel

class Fill_Ad_Event(TimedBaseModel):
    __tablename__ = 'fill_Ad_Event'
    photo = Column(Text)
    name = Column(String(200))
    date_event = Column(String(200))
    time_event = Column(String(50))
    description_event = Column(String(3000))
    person = Column(String(100))
    chat_id_list = Column(ARRAY(String(100)))

    query: sql.select