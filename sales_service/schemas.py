import datetime
import decimal
import re
import uuid

from pydantic import BaseModel, constr, validator


class SellerDetail(BaseModel):
    id: uuid.UUID
    name: str
    cpf: str
    email: str

    class Config:
        orm_mode = True


class SellerCreate(BaseModel):
    name: constr(max_length=255)
    cpf: constr(max_length=14)
    email: constr(max_length=255)
    password: constr(max_length=24)

    @validator("cpf")
    def cpf_number_sanitization(cls, value):
        sanitized_value = re.sub(r"\D", "", value)
        if len(sanitized_value) != 11:
            raise ValueError("Invalid CPF number")

        return sanitized_value

    @validator("email")
    def email_format_validation(cls, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email")

        return value


class SellerAuth(BaseModel):
    email: str
    password: str


class OrderDetail(BaseModel):
    id: uuid.UUID
    code: str
    amount: decimal.Decimal
    timestamp: datetime.datetime
    cpf: str

    class Config:
        orm_mode = True


class OrderCreate(BaseModel):
    code: constr(max_length=255)
    amount: decimal.Decimal
    timestamp: datetime.datetime
    cpf: constr(max_length=14)
