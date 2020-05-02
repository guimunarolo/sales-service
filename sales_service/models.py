import uuid

from sqlalchemy import Column, String
from sqlalchemy_utils.types import PasswordType, UUIDType

from .db import Base


def create_uuid():
    return str(uuid.uuid4())


class Seller(Base):
    __tablename__ = "sellers"

    id = Column(UUIDType(binary=False), primary_key=True, default=create_uuid)
    name = Column(String(255))
    cpf = Column(String(11), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(PasswordType(schemes=["pbkdf2_sha512", "md5_crypt"], deprecated=["md5_crypt"]))
