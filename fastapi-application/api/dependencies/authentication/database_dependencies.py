from typing import Annotated, TYPE_CHECKING

from fastapi import Depends

from core.models import AccessToken, User
from core.db_helper import db_helper


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_tokens_db(session: Annotated["AsyncSession", Depends(db_helper.session_getter)]):
    yield AccessToken.get_db(session=session)


async def get_users_db(session: Annotated["AsyncSession", Depends(db_helper.session_getter)]):
    yield User.get_db(session=session)
