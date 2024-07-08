from sqlalchemy import  Column, Integer, String,Float,Date,DateTime,func
from sqlalchemy.orm import relationship
from .database import Base
from .timestamp import Timestamp


class Budget(Base,Timestamp):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True)
    amount =  Column(Float)
    name = Column(String(100))
    date_from = Column(Date)
    date_to  = Column(Date)
    
    invoices = relationship("Invoice", back_populates="budget")