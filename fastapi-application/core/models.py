from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTable, SQLAlchemyAccessTokenDatabase

from sqlalchemy import MetaData, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, Mapped

from core.mixins import IdIntPkMixin
from core.config import settings


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.db.naming_convention)

    @declared_attr.directive
    @classmethod
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    pass

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[int]):
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
