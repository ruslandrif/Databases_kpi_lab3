from sqlalchemy import Column, VARCHAR, Integer, ForeignKey, Text
from tables.base import BaseModel

class Project(BaseModel):
    __tablename__ = 'Project'
    Name = Column(Text,nullable = False)
    UsersAmount = Column(Integer,nullable = False)
    FoundationYear = Column(Integer,nullable = False)