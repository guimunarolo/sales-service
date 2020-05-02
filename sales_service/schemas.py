import re
import uuid

from pydantic import BaseModel, validator


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
