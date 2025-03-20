import logging
from typing import TYPE_CHECKING, Annotated, Optional


from fastapi import Depends
from fastapi_users import BaseUserManager, IntegerIDMixin

from api.dependencies.authentication.database_dependencies import get_users_db
from core.config import settings
from core.models import User
from webhooks.user import send_new_user_notification

log = logging.getLogger(__name__)

if TYPE_CHECKING:
    from fastapi import Request
    from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(self, user: User, request: Optional["Request"] = None):
        log.warning("User %r has registered.", user.id)

        await send_new_user_notification(user)

    async def on_after_request_verify(self, user: User, token: str, request: Optional["Request"] = None):
        log.warning("Verification requestet for user %r. Verification token: %r", user.id, token)

    async def on_after_forgot_password(self, user: User, token: str, request: Optional["Request"] = None):
        log.warning("User %r has forgot their password. Reset token: %r", user.id, token)

    async def on_after_reset_password(self, user: User, request: Optional["Request"] = None):
        print("User %r has reset their password.", user.id)


async def get_user_manager(user_db: Annotated["SQLAlchemyAccessTokenDatabase", Depends(get_users_db)]):
    yield UserManager(user_db)
