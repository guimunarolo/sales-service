import pytest
from fastapi.testclient import TestClient
from sales_service.db import Base, engine
from sales_service.main import app


@app.on_event("shutdown")
async def shutdown():
    Base.metadata.drop_all(engine)


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture
def seller_create_payload():
    return {
        "name": "João da Silva",
        "email": "joao.silva@gmail.com",
        "cpf": "39824458877",
        "password": "teste123",
    }


@pytest.fixture
def order_create_payload():
    return {
        "code": "123ABC",
        "amount": 1504.47,
        "timestamp": "2020-12-30T12:03:00",
        "cpf": "39824458877",
    }
