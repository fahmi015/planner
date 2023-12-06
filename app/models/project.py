from sqlalchemy import  Column, Integer, String,Float,Date,Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from .timestamp import Timestamp

class Project(Base,Timestamp):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    amount =  Column(Float)
    title =  Column(String(100))
    description = Column(String(500))
    objectives = Column(String(500))
    date_from = Column(Date)
    date_to  = Column(Date)
    type =  Column(String(50))
    budget_id = Column(Integer, ForeignKey("budgets.id"))
    
    #budget = relationship("Budget", back_populates="project")
    tasks = relationship('Task', back_populates='project',lazy='dynamic')
    users = relationship("User", secondary="project_users", back_populates='projects')
    
    
project_userss = Table('project_users', Base.metadata,
    Column('project_id', ForeignKey('projects.id'), primary_key=True),
    Column('user_id', ForeignKey('users.id'), primary_key=True)
)
    