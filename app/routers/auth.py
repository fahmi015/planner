from fastapi import APIRouter, Depends,Body, HTTPException
from ..api.schemas.user import UserLoginSchema
from ..models.database import SessionLocal
from ..dependcies import get_db
from ..api.services.auth.auth import auth

router = APIRouter(
    prefix="/api/auth",
)



@router.post("/login", tags=["auth"])
def login(user_schema: UserLoginSchema = Body(...),db:SessionLocal=Depends(get_db)):
    return auth(user_schema,db)