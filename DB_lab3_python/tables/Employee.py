from sqlalchemy import Column, VARCHAR, Integer, ForeignKey, String
from tables.base import BaseModel
from tables.Team import Team
from tables.Position import Position

class Employee(BaseModel):
    __tablename__ = 'Employee'
    PassportNumber = Column(String,nullable = False)
    #employee_id = Column(Integer, ForeignKey('employees.id', ondelete='CASCADE'), nullable=False, index=True)
    FirstName = Column(String,nullable = False)
    LastName = Column(String,nullable = False)
    TeamId = Column(Integer,ForeignKey('Team.id', ondelete='CASCADE'),nullable = False)
    PositionId = Column(Integer,ForeignKey('Position.id', ondelete='CASCADE'),nullable = False)