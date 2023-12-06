from .base import BaseRepository
from ...models.task import Task
from ..schemas.task import TaskOutSchema,TaskSchema
from typing import List

class TaskRepository(BaseRepository):
    
    def index(db)->List[TaskOutSchema]:
        return db.query(Task).all()
    
    
    def show(id:int,db)->TaskOutSchema:
        return db.query(Task).filter(Task.id==id).first()    
    
    def delete(id:int,db)->TaskOutSchema:
        task=db.query(Task).filter(Task.id==id).first()  
        db.delete(task)
        db.commit()
        return task  
    
    def create(schema:TaskSchema,db)->TaskOutSchema:
        task=Task(**schema.dict())
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    
    
    def update(id:int,schema:TaskSchema,db)->TaskOutSchema:
        task=db.query(Task).filter(Task.id==id).first()  
        task.amount = schema.amount or task.amount
        task.task = schema.task or task.task
        task.title = schema.title or task.title
        task.type = schema.type or task.type
        task.status = schema.status or task.status
        task.date_from = schema.date_from or task.date_from
        task.date_to = schema.date_to or task.date_to
        task.due = schema.due or task.due
        db.commit()
        db.refresh(task)
        return task
    
    
    def update_status(id:int,status,db):
        task=db.query(Task).filter(Task.id==id).first()  
        task.status = status
        db.commit()
        db.refresh(task)
        return task