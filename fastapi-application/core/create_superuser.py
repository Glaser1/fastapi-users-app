import asyncio
import contextlib
import os


from api.api_v1.schemas import UserCreate
from api.dependencies.user_manager import UserManager, get_user_manager
from api.dependencies.database_dependencies import get_users_db
from core.models import User
from core.db_helper import db_helper

get_user_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

defalut_email = os.getenv("DEFAULT_EMAIL", "admin@admin.com")
defalut_password = os.getenv("DEFAULT_PASSWORD", "abc")
defalut_is_active = True
defalut_is_superuser = True
defalut_is_verified = True


async def create_user(user_manager: UserManager, user_create: UserCreate) -> User:
    user: User = await user_manager.create(user_create=user_create, safe=False)
    return user


async def create_superuser(
    email: str = defalut_email,
    password: str = defalut_password,
    is_active: bool = defalut_is_active,
    is_superuser: bool = defalut_is_superuser,
    is_verified: bool = defalut_is_verified,
):

    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )

    async with db_helper.session_factory() as session:
        async with get_user_db_context(session) as users_db:
            async with get_user_manager_context(users_db) as user_manager:
                return await create_user(user_manager, user_create)


if __name__ == "__main__":
    asyncio.run(create_superuser())
