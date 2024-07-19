from fastapi import APIRouter,Depends
from .budget import router as budget
from .project import router as project
from .task import router as task
from .user import router as user
from .invoice import router as invoice
from .permission import router as permission
from ..api.services.auth.auth_bearer import JWTBearer


router = APIRouter(
    prefix="/api/user",
    dependencies=[Depends(JWTBearer())]
)
router.include_router(budget)
router.include_router(project)
router.include_router(task)
router.include_router(user)
router.include_router(invoice)
router.include_router(permission)

