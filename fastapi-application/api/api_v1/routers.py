from fastapi import APIRouter

from core.config import settings
from api.api_v1.fastapi_users import fastapi_users
from api.api_v1.schemas import UserRead, UserCreate, UserUpdate
from api.dependencies.backend import authentication_backend

auth_router = APIRouter(prefix=settings.api.v1.auth, tags=["Auth"])

# /login
# /logout
auth_router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)

# /register
auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

# /me
# /{user_id}
users_router = APIRouter(prefix=settings.api.v1.users, tags=["Users"])
users_router.include_router(
    router=fastapi_users.get_users_router(UserRead, UserUpdate),
)


# /request-verify-token
# /verify
auth_router.include_router(
    router=fastapi_users.get_verify_router(UserRead),
)

# /forgot-password
# /reset-password
auth_router.include_router(router=fastapi_users.get_reset_password_router())
