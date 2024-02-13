from abc import ABC, abstractmethod

from config.db import session_maker
from source.models import Files
from sqlalchemy import insert, select

__all__ = ("AbstractRepository", "FilesRepository", "SQLAlchemyRepository")


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, data):
        raise NotImplementedError

    @abstractmethod
    def find(self, pk: int):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    """Represents a repository that aims to interact with database queries."""

    model = None

    def add(self, data: dict) -> int:
        with session_maker() as session:
            statement = insert(table=self.model).values(**data).returning(self.model)
            result = session.execute(statement)
            session.commit()
            return result.scalar_one()

    def find(self, pk: int) -> list:
        with session_maker() as session:
            statement = select(self.model)
            res = session.execute(statement).all()
            return [row[0].to_json() for row in res]


class FilesRepository(SQLAlchemyRepository):
    """Represents a repository designed to interact with files based on `SQLAlchemyRepository`."""

    model = Files
