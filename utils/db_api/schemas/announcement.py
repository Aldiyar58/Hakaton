from sqlalchemy import Column, BigInteger, String, sql, Text

from utils.db_api.db_gino import TimedBaseModel

class Fill_Ad_Event(TimedBaseModel):
    __tablename__ = 'fill_Ad_Event'
    photo = Column(Text)
    date_event = Column(String(200))
    time_event = Column(String(50))
    description_event = Column(String(3000))
    query: sql.select