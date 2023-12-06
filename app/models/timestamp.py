from sqlalchemy import  Column,DateTime,func


class Timestamp():
   
    created_at = Column(DateTime,default=func.now())
    updated_at = Column(DateTime,onupdate=func.now())

