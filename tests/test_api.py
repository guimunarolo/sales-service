import uuid

from fastapi import status


def test_sellers_create(client, seller_create_payload):
    response = client.post("/sellers/", json=seller_create_payload)
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert uuid.UUID(response_data["id"])
    assert response_data["name"] == seller_create_payload["name"]
    assert response_data["email"] == seller_create_payload["email"]
    assert response_data["cpf"] == seller_create_payload["cpf"]
    assert response_data["password"] == seller_create_payload["password"]
