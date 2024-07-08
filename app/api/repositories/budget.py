from .base import BaseRepository
from ...models.budget import Budget
from ..schemas.budget import BudgetOutSchema,BudgetSchema
from typing import List

class BudgetRepository(BaseRepository):
    
    def index(db)->List[BudgetOutSchema]:
        return db.query(Budget).all()
    
    
    def show(id:int,db)->BudgetOutSchema:
        return db.query(Budget).filter(Budget.id==id).first()    
    
    def delete(id:int,db):
        budget=db.query(Budget).filter(Budget.id==id).first()  
        db.delete(budget)
        db.commit()
        return budget  
    
    
    def create(schema:BudgetSchema,db)->BudgetOutSchema:
        budget=Budget(**schema.dict())
        db.add(budget)
        db.commit()
        db.refresh(budget)
        return budget
    
    
    def update(id:int,schema:BudgetSchema,db)->BudgetOutSchema:
        budget=db.query(Budget).filter(Budget.id==id).first()  
        budget.amount = schema.amount or budget.amount
        budget.name = schema.name or budget.name
        budget.date_from = schema.date_from or budget.date_from
        budget.date_to = schema.date_to or budget.date_to
        db.add(budget)
        db.commit()
        db.refresh(budget)
        return budget