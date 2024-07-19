from .base import BaseRepository
from ...models.invoice import Invoice
from ..schemas.invoice import InvoiceOutSchema,InvoiceSchema
from typing import List

class InvoiceRepository(BaseRepository):
    
    def index(db)->List[InvoiceOutSchema]:
        return db.query(Invoice).all()
    
    
    def show(id:int,db)->InvoiceOutSchema:
        return db.query(Invoice).filter(Invoice.id==id).first()    
    
    def delete(id:int,db):
        invoice=db.query(Invoice).filter(Invoice.id==id).first()  
        db.delete(invoice)
        db.commit()
        return invoice  
    
    
    def create(schema:InvoiceSchema,db)->InvoiceOutSchema:
        invoice=Invoice(**schema.dict())
        db.add(invoice)
        db.commit()
        db.refresh(invoice)
        return invoice
    
    
    def update(id:int,schema:InvoiceSchema,db)->InvoiceOutSchema:
        invoice=db.query(Invoice).filter(Invoice.id==id).first()  
        invoice.amount = schema.amount or invoice.amount
        invoice.details = schema.details or invoice.details
        invoice.status = schema.status or invoice.status

        db.add(invoice)
        db.commit()
        db.refresh(invoice)
        return invoice