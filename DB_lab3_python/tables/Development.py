from sqlalchemy import Column, VARCHAR, Integer, ForeignKey
from tables.base import BaseModel

from tables.Team import Team 
from tables.Project import Project

class Development(BaseModel):
    __tablename__ = 'Development'
    ProjectId = Column(Integer,ForeignKey('Project.id'),nullable = False)
    TeamId = Column(Integer,ForeignKey('Team.id'),nullable = False)