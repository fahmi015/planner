from fastapi import APIRouter, Depends,Body, HTTPException
from ..api.repositories.project import ProjectRepository
from ..dependcies import get_db
from ..models.database import SessionLocal
from ..api.schemas.project import ProjectSchema,ProjectOutSchema
from typing import List

router = APIRouter(
    prefix="/projects",
    tags=["projects"]
)

@router.get("/",response_model=List[ProjectOutSchema])
def index(db:SessionLocal=Depends(get_db)):
    return ProjectRepository.index(db)


@router.get("/{id}")
def show(id:int,db:SessionLocal=Depends(get_db)):
    return ProjectRepository.show(id,db)


@router.post("/")
def store(ProjectSchema:ProjectSchema,db:SessionLocal=Depends(get_db)):
    budget_repository=ProjectRepository.create(ProjectSchema,db)
    return budget_repository


@router.put("/{id}")
def update(id:int,ProjectSchema:ProjectSchema,db:SessionLocal=Depends(get_db)):
    return ProjectRepository.update(id,ProjectSchema,db)

@router.delete("/{id}")
def delete(id:int,db:SessionLocal=Depends(get_db)):
    return ProjectRepository.delete(id,db)