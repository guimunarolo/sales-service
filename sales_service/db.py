import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from .configs import settings

engine = sqlalchemy.create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
session = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))
metadata = sqlalchemy.MetaData()
Base = declarative_base()
