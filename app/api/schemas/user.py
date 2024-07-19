from pydantic import BaseModel, Field
from datetime import datetime
from .invoice import InvoiceOutSchema
from .permission import PermissionOutSchema
from typing import List

class UserSchema(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    username: str = Field(...)
    avatar: str|None = Field(...)
   
    
    
class PermissionSchema(BaseModel):
    permissions_id:List[int] | None = Field(...)

class UserUpdateSchema(UserSchema,PermissionSchema):
    pass
    
    
class PasswordSchema(BaseModel):
    password: str = Field(default="password",min_length=3)
          
class UserLoginSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(default="password",min_length=3)
    

class UserInSchema(UserSchema,PasswordSchema,PermissionSchema):
    pass  
        
class UserOutSchema(UserSchema):
    id:int
    created_at:datetime|None 
    updated_at:datetime|None
    last_login:datetime|None
    
    tasks: List[InvoiceOutSchema] = []
    permissions: List[PermissionOutSchema] = []
    
    class Config:
        from_attributes = True
