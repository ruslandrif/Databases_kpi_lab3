from sqlalchemy import Column, VARCHAR, Integer, ForeignKey, String
from tables.base import BaseModel

class Buyer(BaseModel):
    __tablename__ = 'Buyer'
    country = Column(String,nullable = False)