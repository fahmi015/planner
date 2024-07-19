from pydantic import BaseModel, Field
from datetime import datetime,date
from typing import List
from .invoice import InvoiceOutSchema

class BudgetSchema(BaseModel):
    amount: float = Field(...)
    name: str = Field(...)
    date_from: date = Field(...)
    date_to: date = Field(...)
        
    
class BudgetOutSchema(BaseModel):
    id:int
    amount: float = Field(...)
    name: str = Field(...)
    date_from: date = Field(...)
    date_to: date = Field(...)
    invoices: List[InvoiceOutSchema] = []
    created_at:datetime | None 
    updated_at:datetime | None

    class Config:
        #orm_mode = True
        from_attributes = True