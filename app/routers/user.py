from fastapi import APIRouter, Depends,Body,HTTPException,Header
from ..api.repositories.user import UserRepository
from ..dependcies import get_db
from ..models.database import SessionLocal
from ..api.schemas.user import UserSchema,UserUpdateSchema,UserInSchema,PasswordSchema,UserOutSchema
from ..api.services.auth.auth_handler import expirationDataJWT
from ..api.services.auth.auth_bearer import JWTBearer
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["users"]
) 

@router.get("/permissions",response_model=UserOutSchema)
async def index(db:SessionLocal=Depends(get_db),token: str=Depends(JWTBearer())):
    return UserRepository.permissions(db,token)

@router.get("/",response_model=List[UserOutSchema])
async def index(db:SessionLocal=Depends(get_db)):
    return UserRepository.index(db)

@router.get("/token-creation-date")
async def get_token_creation_date(token: str=Depends(JWTBearer())):
    return {"created_at":expirationDataJWT(token)}

@router.put("/{id}/update-password",response_model=UserOutSchema)
async def update(id:int,current_password:str=Body(...),new_password:str=Body(...),db:SessionLocal=Depends(get_db)):
    return UserRepository.update_password(id,current_password,new_password,db)


@router.put("/{id}/force-update-password",response_model=UserOutSchema)
async def update(id:int,PasswordSchema:PasswordSchema ,db:SessionLocal=Depends(get_db)):
    return UserRepository.force_password(id,PasswordSchema.password,db)

@router.get("/{id}",response_model=UserOutSchema)
async def show(id:int,db:SessionLocal=Depends(get_db)):
    return UserRepository.show(id,db)


@router.post("/",response_model=UserOutSchema)
async def store(UserSchema:UserInSchema,db:SessionLocal=Depends(get_db)):
    budget_repository=UserRepository.create(UserSchema,db)
    return budget_repository

@router.put("/{id}",response_model=UserOutSchema)
async def update(id:int,UserSchema:UserUpdateSchema,db:SessionLocal=Depends(get_db)):
    return UserRepository.update(id,UserSchema,db)

@router.delete("/{id}",response_model=UserOutSchema)
async def delete(id:int,db:SessionLocal=Depends(get_db)):
    return UserRepository.delete(id,db)




