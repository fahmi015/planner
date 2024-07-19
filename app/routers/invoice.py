from fastapi import APIRouter, Depends,Body, HTTPException
from ..api.repositories.invoice import InvoiceRepository
from ..dependcies import get_db
from ..models.database import SessionLocal
from ..api.schemas.invoice import InvoiceSchema

router = APIRouter(
    prefix="/invoices",
    tags=["invoice"]
)

@router.get("/")
def index(db:SessionLocal=Depends(get_db)):
    return InvoiceRepository.index(db)


@router.get("/{id}")
def show(id:int,db:SessionLocal=Depends(get_db)):
    return InvoiceRepository.show(id,db)


@router.post("/")
def store(InvoiceSchema:InvoiceSchema,db:SessionLocal=Depends(get_db)):
    budget_repository=InvoiceRepository.create(InvoiceSchema,db)
    return budget_repository


@router.put("/{id}")
def update(id:int,InvoiceSchema:InvoiceSchema,db:SessionLocal=Depends(get_db)):
    return InvoiceRepository.update(id,InvoiceSchema,db)

@router.delete("/{id}")
def delete(id:int,db:SessionLocal=Depends(get_db)):
    return InvoiceRepository.delete(id,db)