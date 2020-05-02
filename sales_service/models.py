import uuid

from pydantic import BaseModel


class SellerDetail(BaseModel):
    id: uuid.UUID
    name: str
    cpf: str
    email: str
    password: str


class SellerCreate(BaseModel):
    name: str
    cpf: str
    email: str
    password: str
