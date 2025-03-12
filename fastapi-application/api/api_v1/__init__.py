from fastapi import APIRouter

from core.config import settings
from api.api_v1.routers import router as auth_router

router = APIRouter(prefix=settings.api.v1.prefix)
router.include_router(auth_router)
