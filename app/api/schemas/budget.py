from pydantic import BaseModel, Field
from datetime import datetime,date

class BudgetSchema(BaseModel):
    amount: float = Field(...)
    name: str = Field(...)
    date_from: date = Field(...)
    date_to: date = Field(...)

    class Config:
        from_attributes = True
        
class BudgetOutSchema(BudgetSchema):
    id:int
    created_at:datetime | None 
    updated_at:datetime | None