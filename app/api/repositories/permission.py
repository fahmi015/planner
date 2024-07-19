from .base import BaseRepository
from ...models.permission import Permission
from ..schemas.permission import PermissionOutSchema,PermissionSchema
from typing import List

class PermissionRepository(BaseRepository):
    
    def index(db)->List[PermissionOutSchema]:
        return db.query(Permission).all()
    
    
    def show(id:int,db)->PermissionOutSchema:
        return db.query(Permission).filter(Permission.id==id).first()    
    
    def delete(id:int,db):
        permission=db.query(Permission).filter(Permission.id==id).first()  
        db.delete(permission)
        db.commit()
        return permission  
    
    def create(schema:PermissionSchema,db)->PermissionOutSchema:
        permission=Permission(**schema.dict())
        db.add(permission)
        db.commit()
        db.refresh(permission)
        return Permission
    
    def update(id:int,schema:PermissionSchema,db)->PermissionOutSchema:
        permission=db.query(Permission).filter(Permission.id==id).first()  
        permission.name = schema.name or permission.name
       
        db.add(permission)
        db.commit()
        db.refresh(permission)
        return permission