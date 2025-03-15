import logging
from typing import Annotated, Optional, TYPE_CHECKING

from fastapi import Depends
from fastapi_users import BaseUserManager, IntegerIDMixin

from core.models import User
from api.dependencies.database_dependencies import get_users_db
from core.config import settings

log = logging.getLogger(__name__)

if TYPE_CHECKING:
    from fastapi import Request
    from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(self, user: User, request: Optional["Request"] = None):
        log.warning("User %r has registered.", user.id)

    async def on_after_request_verify(self, user: User, token: str, request: Optional["Request"] = None):
        log.warning("Verification requestet for user %r. Verification token: %r", user.id, token)

    async def on_after_forgot_password(self, user: User, token: str, request: Optional["Request"] = None):
        log.warning("User %r has forgot their password. Reset token: %r", user.id, token)

    async def on_after_reset_password(self, user: User, request: Optional["Request"] = None):
        print("User %r has reset their password.", user.id)


async def get_user_manager(user_db: Annotated["SQLAlchemyAccessTokenDatabase", Depends(get_users_db)]):
    yield UserManager(user_db)
