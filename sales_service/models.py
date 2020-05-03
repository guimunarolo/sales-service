import uuid

from sqlalchemy import Column, DateTime, Float, String
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


class Order(Base):
    __tablename__ = "orders"

    id = Column(UUIDType(binary=False), primary_key=True, default=create_uuid)
    cpf = Column(String(11), index=True)
    code = Column(String(255))
    amount = Column(Float(asdecimal=True))
    timestamp = Column(DateTime())
    status = Column(String(255), default="")
