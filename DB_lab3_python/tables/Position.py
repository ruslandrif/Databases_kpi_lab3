from sqlalchemy import Column, VARCHAR, Integer, ForeignKey, Interval
from tables.base import BaseModel

class Position(BaseModel):
    __tablename__ = 'Position'
    salary = Column(Integer,nullable = False) 
    WorkingHours = Column(Interval,nullable = False) 