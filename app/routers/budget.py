from fastapi import APIRouter, Depends,Body, HTTPException
from ..api.repositories.budget import BudgetRepository
from ..dependcies import get_db
from ..models.database import SessionLocal
from ..api.schemas.budget import BudgetSchema

router = APIRouter(
    prefix="/budgets",
    tags=["budgets"]
)

@router.get("/")
def index(db:SessionLocal=Depends(get_db)):
    return BudgetRepository.index(db)


@router.get("/{id}")
def show(id:int,db:SessionLocal=Depends(get_db)):
    return BudgetRepository.show(id,db)


@router.post("/")
def store(BudgetSchema:BudgetSchema,db:SessionLocal=Depends(get_db)):
    budget_repository=BudgetRepository.create(BudgetSchema,db)
    return budget_repository


@router.put("/{id}")
def update(id:int,BudgetSchema:BudgetSchema,db:SessionLocal=Depends(get_db)):
    return BudgetRepository.update(id,BudgetSchema,db)

@router.delete("/{id}")
def delete(id:int,db:SessionLocal=Depends(get_db)):
    return BudgetRepository.delete(id,db)