from .base import BaseRepository
from ...models.user import User
from ..schemas.user import UserOutSchema,UserSchema,UserInSchema
from ..services.auth.auth import verify_password,hash_password
from fastapi import HTTPException
from typing import List

class UserRepository(BaseRepository):
    
    def index(db)->List[UserOutSchema]:
        return db.query(User).all() 
    
    
    def show(id:int,db)->UserOutSchema:
        return db.query(User).filter(User.id==id).first()    
    
    def delete(id:int,db)->UserOutSchema:
        user=db.query(User).filter(User.id==id).first()  
        db.delete(user)
        db.commit()
        return user  
    
    def create(schema:UserInSchema,db)->UserOutSchema:
        user=User(avatar=schema.avatar,username=schema.username, first_name=schema.first_name,last_name=schema.last_name,password = hash_password(schema.password))
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    
    def update(id:int,schema:UserSchema,db)->UserOutSchema:
        user=db.query(User).filter(User.id==id).first()  
        if user is None:
            raise HTTPException(status_code=404, detail="Item not found")
        user.username = schema.username or user.username
        user.first_name = schema.first_name or user.first_name
        user.last_name = schema.last_name or user.last_name
        user.avatar = schema.avatar or user.avatar
        db.commit()
        db.refresh(user)
        return user
    
    def update_password(id:int,password:str,new_password:str,db)->UserOutSchema:
        user=db.query(User).filter(User.id==id).first()
        if verify_password(password,user.password):  
            user.password = hash_password(new_password)
       
        db.commit()
        db.refresh(user)
        return user
    
    def force_password(id:int,password:str,db)->UserOutSchema:
        user=db.query(User).filter(User.id==id).first()  
        user.password = hash_password(password)
        db.commit()
        db.refresh(user)
        return user