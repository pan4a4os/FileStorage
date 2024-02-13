from config import settings
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

__all__ = ("Base", "session_maker")

engine: Engine = create_engine(url=settings.DB_URL)

session_maker = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
