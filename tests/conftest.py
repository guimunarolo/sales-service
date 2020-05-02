import pytest
from fastapi.testclient import TestClient
from sales_service.db import engine, metadata
from sales_service.main import app


@app.on_event("shutdown")
async def shutdown():
    metadata.drop_all(engine)


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
