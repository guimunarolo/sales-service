import databases
import sqlalchemy

from .configs import settings

database = databases.Database(settings.DATABASE_URL)
engine = sqlalchemy.create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
metadata = sqlalchemy.MetaData()


sellers_orm = sqlalchemy.Table(
    "sellers",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String(255), primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(255)),
    sqlalchemy.Column("cpf", sqlalchemy.String(11), unique=True, index=True),
    sqlalchemy.Column("email", sqlalchemy.String(255), unique=True, index=True),
    sqlalchemy.Column("password", sqlalchemy.String(255)),
)
