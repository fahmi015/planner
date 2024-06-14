from sqlalchemy import  Column, Integer, String,Float,Date,ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from .timestamp import Timestamp


class Task(Base,Timestamp):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    # amount =  Column(Float)
    title = Column(String(500))
    task = Column(String(500))
    type = Column(String(25))
    status = Column(String(25))
    # date_from = Column(Date)
    # date_to  = Column(Date)
    due = Column(String(25))
    
    project_id = Column(Integer, ForeignKey("projects.id"))
    #project = relationship("Project", back_populates="task")
    project = relationship('Project', back_populates='tasks')