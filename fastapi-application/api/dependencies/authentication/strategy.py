from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy

from core.config import settings
from api.dependencies.authentication.database_dependencies import get_access_tokens_db

if TYPE_CHECKING:
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase

    from core.models import AccessToken


def get_database_strategy(
    access_tokens_db: Annotated["AccessTokenDatabase[AccessToken]", Depends(get_access_tokens_db)],
):
    return DatabaseStrategy(database=access_tokens_db, lifetime_seconds=settings.access_token.lifetime_seconds)
