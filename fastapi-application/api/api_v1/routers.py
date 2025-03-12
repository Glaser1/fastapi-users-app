from fastapi import APIRouter

from core.config import settings
from api.api_v1.fastapi_users import fastapi_users
from api.dependencies.backend import authentication_backend

router = APIRouter(prefix=settings.api.v1.auth, tags=["Auth"])
router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)
