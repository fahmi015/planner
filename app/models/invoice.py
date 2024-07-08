from sqlalchemy import  Column, Integer, String,DateTime,ForeignKey,Float
from .database import Base
from .timestamp import Timestamp
from sqlalchemy.orm import relationship

class Invoice(Base,Timestamp):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    amount =  Column(Float)
    details = Column(String(500),nullable=True)
    status = Column(String(100))
    
    user_id = Column(Integer, ForeignKey("users.id"))
    budget_id = Column(Integer, ForeignKey("budgets.id"))

    #user = relationship('User', back_populates='invoices')
    budget = relationship('Budget', back_populates='invoices')
    



