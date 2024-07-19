from sqlalchemy import  Column, Integer, String,Float,Date,Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from .timestamp import Timestamp

class Permission(Base,Timestamp):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True)
    name =  Column(String(100))
   
    users = relationship("User", secondary="permission_users", back_populates='permissions')
    
    
permission_users = Table('permission_users', Base.metadata,
    Column('permission_id', ForeignKey('permissions.id'), primary_key=True),
    Column('user_id', ForeignKey('users.id'), primary_key=True)
)
    