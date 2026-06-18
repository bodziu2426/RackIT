from sqlalchemy import Column, Integer, String, Float
from database import Base

class SesjaDB(Base):
    __tablename__ = "sesje"

    id = Column(Integer, primary_key=True)
    entry_date = Column(String)
    workout_date = Column(String)
    session_type = Column(String)
    exercise = Column(String)
    series = Column(Integer)
    weight = Column(Float)
    reps = Column(Integer)
    rir = Column(Integer)