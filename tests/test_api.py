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
