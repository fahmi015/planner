from fastapi import APIRouter, Depends,Body, HTTPException
from ..api.repositories.task import TaskRepository
from ..dependcies import get_db
from ..models.database import SessionLocal
from ..api.schemas.task import TaskSchema


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.get("/")
def index(db:SessionLocal=Depends(get_db)):
    return TaskRepository.index(db)


@router.get("/{id}")
def show(id:int,db:SessionLocal=Depends(get_db)):
    return TaskRepository.show(id,db)


@router.post("/")
def store(TaskSchema:TaskSchema,db:SessionLocal=Depends(get_db)):
    budget_repository=TaskRepository.create(TaskSchema,db)
    return budget_repository

from pydantic import BaseModel
class Item(BaseModel):
    status: str
    
@router.put("/{id}/update-status")
def update_status(id:int,item:Item,db:SessionLocal=Depends(get_db)):
    return TaskRepository.update_status(id,item.status,db)

@router.put("/{id}")
def update(id:int,TaskSchema:TaskSchema,db:SessionLocal=Depends(get_db)):
    return TaskRepository.update(id,TaskSchema,db)

@router.delete("/{id}")
def delete(id:int,db:SessionLocal=Depends(get_db)):
    return TaskRepository.delete(id,db)