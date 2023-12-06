from sqlalchemy import  Column, Integer, String,DateTime
from .database import Base
from .timestamp import Timestamp
from sqlalchemy.orm import relationship

class User(Base,Timestamp):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username =  Column(String(50))
    avatar = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))
    password  = Column(String(100))
    last_login =  Column(DateTime)

    projects = relationship("Project", secondary="project_users", back_populates='users')
