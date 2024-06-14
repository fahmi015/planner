from pydantic import BaseModel, Field
from datetime import datetime,date

        
class TaskSchema(BaseModel):
    # amount: float | None = Field(...)
    task: str = Field(...)
    title: str = Field(...)
    type: str = Field(...)
    status: str = Field(...)
    # date_from: str = Field(...)
    # date_to: str = Field(...)
    due: str = Field(...)
    project_id:int = Field(...)
        
class TaskOutSchema(BaseModel):
    id:int
    created_at:datetime | None 
    updated_at:datetime | None
    # amount: float | None 
    task: str   | None 
    title: str  | None 
    type: str 
    status: str 
    # date_from: date   | None 
    # date_to: date   | None 
    due :str  | None 
    project_id:int 

    class Config:
        from_attributes = True