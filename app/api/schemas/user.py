from pydantic import BaseModel, Field
from datetime import datetime

class UserSchema(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    username: str = Field(...)
    avatar: str|None = Field(...)
    
    
class PasswordSchema(BaseModel):
    password: str = Field(default="password",min_length=3)
          
class UserLoginSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(default="password",min_length=3)
    

class UserInSchema(UserSchema,PasswordSchema):
    pass  
        
class UserOutSchema(UserSchema):
    id:int
    created_at:datetime|None 
    updated_at:datetime|None
    last_login:datetime|None
    
