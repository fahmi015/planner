from pydantic import BaseModel, Field
from datetime import datetime
from datetime import date
from typing import List



class InvoiceSchema(BaseModel):
    details: str = Field(...)
    status: str = Field(...)
    amount:float | None = Field(...) 
    budget_id:int = Field(...)

    
        
class InvoiceOutSchema(BaseModel):
    id:int
    created_at:datetime|None 
    updated_at:datetime|None 
    details: str|None
    status: str|None
    amount: float
    budget_id:int 

    
    class Config:
        from_attributes = True
    
    
    
