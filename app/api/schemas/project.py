from pydantic import BaseModel, Field
from datetime import datetime
from datetime import date
from .task import TaskOutSchema
from .user import UserOutSchema
from typing import List



class ProjectSchema(BaseModel):
    title: str = Field(...)
    date_from: date = Field(...)
    date_to: date = Field(...)
    type:str | None = Field(...)
    users_id:List[int] | None = Field(...)

        
class ProjectOutSchema(BaseModel):
    id:int
    created_at:datetime|None 
    updated_at:datetime|None 
    title: str|None
    date_from: date
    date_to: date
    type:str | None = Field(...)
    tasks: List[TaskOutSchema] = []
    users: List[UserOutSchema] = []
    
    class Config:
        from_attributes = True
    
    
    
