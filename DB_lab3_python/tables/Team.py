from sqlalchemy import Column, VARCHAR, Integer, ForeignKey
from tables.base import BaseModel

class Team(BaseModel):
    __tablename__ = 'Team'