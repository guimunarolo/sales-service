import uuid

import asynctest
from fastapi import status

from .factories import OrderFactory, SellerFactory


def test_sellers_create_successfully(client, seller_create_payload):
    response = client.post("/sellers/", json=seller_create_payload)
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert uuid.UUID(response_data["id"])
    assert response_data["name"] == seller_create_payload["name"]
    assert response_data["email"] == seller_create_payload["email"]
    assert response_data["cpf"] == seller_create_payload["cpf"]
    assert "password" not in response_data


def test_sellers_create_fails_with_registered_email(client, seller_create_payload):
    seller = SellerFactory()
    seller_create_payload["email"] = seller.email

    response = client.post("/sellers/", json=seller_create_payload)
    response_data = response.json()

    assert response.status_code == status.HTTP_409_CONFLICT
    assert response_data["detail"] == "This email is already registered"


def test_sellers_create_fails_with_registered_cpf(client, seller_create_payload):
    seller = SellerFactory()
    seller_create_payload["cpf"] = seller.cpf

    response = client.post("/sellers/", json=seller_create_payload)
    response_data = response.json()

    assert response.status_code == status.HTTP_409_CONFLICT
    assert response_data["detail"] == "This CPF is already registered"


def test_sellers_list_successfully(client):
    seller = SellerFactory()

    response = client.get("/sellers/")
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_data) == 1
    assert response_data[0]["id"] == seller.id


def test_sellers_authentication_successfully(client):
    seller = SellerFactory(password="test123")

    response = client.post("/sellers/authentication/", json={"email": seller.email, "password": "test123"})
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_data["id"] == seller.id


def test_sellers_authentication_with_wrong_password(client):
    seller = SellerFactory(password="test123")

    response = client.post("/sellers/authentication/", json={"email": seller.email, "password": "wrong123"})

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_sellers_authentication_with_unnexistent_email(client):
    SellerFactory(email="test.123@gmail.com", password="test123")

    response = client.post(
        "/sellers/authentication/", json={"email": "wrong@gmail.com", "password": "test123"}
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_orders_create_successfully(client, order_create_payload):
    response = client.post("/orders/", json=order_create_payload)
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert uuid.UUID(response_data["id"])
    assert response_data["code"] == order_create_payload["code"]
    assert response_data["amount"] == order_create_payload["amount"]
    assert response_data["timestamp"] == order_create_payload["timestamp"]
    assert response_data["cpf"] == order_create_payload["cpf"]
    assert "status" in response_data
    assert "cashback_percentage" in response_data
    assert "cashback_amount" in response_data


def test_orders_list_successfully(client):
    order = OrderFactory()

    response = client.get("/orders/")
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_data) == 1
    assert response_data[0]["id"] == order.id


@asynctest.patch("sales_service.clients.CashbackClient.get_cashback")
def test_cashback_successfully(get_cashback_mock, client):
    get_cashback_mock.return_value = 50
    OrderFactory(cashback_amount=150, cpf="12345678910")
    OrderFactory(cashback_amount=150, cpf="12345678910")

    response = client.get("/cashback/", params={"cpf": "12345678910"})
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_data["legacy_amount"] == 50.00
    assert response_data["orders_amount"] == 300.00
    assert response_data["total"] == 350.00
