from fastapi import APIRouter, Depends,Body, HTTPException
from ..api.repositories.permission import PermissionRepository
from ..dependcies import get_db
from ..models.database import SessionLocal
from ..api.schemas.permission import PermissionSchema

router = APIRouter(
    prefix="/permissions",
    tags=["permission"]
)

@router.get("/")
def index(db:SessionLocal=Depends(get_db)):
    return PermissionRepository.index(db)


@router.get("/{id}")
def show(id:int,db:SessionLocal=Depends(get_db)):
    return PermissionRepository.show(id,db)


@router.post("/")
def store(PermissionSchema:PermissionSchema,db:SessionLocal=Depends(get_db)):
    budget_repository=PermissionRepository.create(PermissionSchema,db)
    return budget_repository


@router.put("/{id}")
def update(id:int,PermissionSchema:PermissionSchema,db:SessionLocal=Depends(get_db)):
    return PermissionRepository.update(id,PermissionSchema,db)

@router.delete("/{id}")
def delete(id:int,db:SessionLocal=Depends(get_db)):
    return PermissionRepository.delete(id,db)