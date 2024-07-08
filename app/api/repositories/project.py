from .base import BaseRepository
from ...models.project import Project
from ..schemas.project import ProjectOutSchema,ProjectSchema
from ...models.user import User
from typing import List
from fastapi import HTTPException
from ..services.auth.auth_handler import getUserId

from fastapi import Depends

class ProjectRepository(BaseRepository):
    
    def index(db,token)->List[ProjectOutSchema]:
        
        user_id = getUserId(token)
        return db.query(User).filter(User.id==user_id).first().projects
        #return db.query(Project).all()
     
    
    def show(id:int,db)->ProjectOutSchema:
        return db.query(Project).filter(Project.id==id).first()    
    
    def delete(id:int,db)->ProjectOutSchema:
        project=db.query(Project).filter(Project.id==id).first()  
        db.delete(project)
        db.commit()
        return project  
    
    def create(schema:ProjectSchema,db)->ProjectOutSchema:
        project_data = {k: v for k, v in schema.dict().items() if k != 'users_id'}
        project=Project(**project_data)
        for id in schema.users_id:
            user = db.query(User).filter(User.id == id).first()
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            project.users.append(user)
            
        db.add(project)
        db.commit()
        db.refresh(project)
        return project
    
    
    def update(id:int,schema:ProjectSchema,db)->ProjectOutSchema:
        project=db.query(Project).filter(Project.id==id).first()  
        project.amount = schema.amount or project.amount
        project.title = schema.title or project.title
        project.description = schema.description or project.description
        project.date_from = schema.date_from or project.date
        project.date_to = schema.date_to or project.date_to
        project.type = schema.type or project.type
        db.add(project)
        db.commit()
        db.refresh(project)
        return project