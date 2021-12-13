from sqlalchemy import Column, VARCHAR, Integer, ForeignKey, String
from tables.base import BaseModel
from tables.Buyer import Buyer 
from tables.Project import Project

class ProjectOrder(BaseModel):
    __tablename__ = 'Project order'
    price = Column(String,nullable = False)
    BuyerId = Column(Integer, ForeignKey('Buyer.id', ondelete='CASCADE'), nullable=False)
    ProjectId = Column(Integer,ForeignKey('Project.id', ondelete='CASCADE'),nullable = False)