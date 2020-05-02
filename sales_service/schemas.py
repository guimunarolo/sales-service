import uuid

from pydantic import BaseModel


class SellerDetail(BaseModel):
    id: uuid.UUID
    name: str
    cpf: str
    email: str

    class Config:
        orm_mode = True


class SellerCreate(BaseModel):
    name: str
    cpf: str
    email: str
    password: str


class SellerAuth(BaseModel):
    email: str
    password: str
