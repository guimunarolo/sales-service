import uuid

from fastapi import status

from .factories import SellerFactory


def test_sellers_create(client, seller_create_payload):
    response = client.post("/sellers/", json=seller_create_payload)
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert uuid.UUID(response_data["id"])
    assert response_data["name"] == seller_create_payload["name"]
    assert response_data["email"] == seller_create_payload["email"]
    assert response_data["cpf"] == seller_create_payload["cpf"]
    assert "password" not in response_data


def test_sellers_list(client):
    seller = SellerFactory()

    response = client.get("/sellers/")
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_data) == 1
    assert response_data[0]["id"] == seller.id


def test_sellers_authentication(client):
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
