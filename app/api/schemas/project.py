from pydantic import BaseModel, Field
from datetime import datetime
from datetime import date
from .task import TaskOutSchema
from .user import UserOutSchema
from typing import List



class ProjectSchema(BaseModel):
    amount: float = Field(...)
    title: str = Field(...)
    description: str | None = Field(...)
    objectives: str | None = Field(...)
    date_from: date = Field(...)
    date_to: date = Field(...)
    budget_id:int = Field(...)
    type:str | None = Field(...)
    users_id:List[int] | None = Field(...)
    
    

    
        
class ProjectOutSchema(BaseModel):
    id:int
    created_at:datetime|None 
    updated_at:datetime|None 
    amount: float
    title: str|None
    description: str|None
    date_from: date
    date_to: date
    budget_id:int
    type:str | None = Field(...)
    tasks: List[TaskOutSchema] = []
    users: List[UserOutSchema] = []
    
    class Config:
        from_attributes = True
    
    
    
