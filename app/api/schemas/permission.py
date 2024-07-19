from pydantic import BaseModel, Field
from datetime import datetime
from datetime import date
#from .user import UserOutSchema
from typing import List

class PermissionSchema(BaseModel):
    name: str = Field(...)

        
class PermissionOutSchema(BaseModel):
    id:int
    created_at:datetime|None 
    updated_at:datetime|None 
    name: str|None
    #users: List[UserOutSchema] = []
    
    # class Config:
    #     from_attributes = True
    
    
    
