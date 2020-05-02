import databases
import sqlalchemy

from .configs import settings

database = databases.Database(settings.DATABASE_URL)
engine = sqlalchemy.create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
metadata = sqlalchemy.MetaData()
