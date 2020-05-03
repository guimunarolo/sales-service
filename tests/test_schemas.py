from decimal import Decimal

import pytest
from pydantic import ValidationError
from sales_service.schemas import ORDER_SELF_APPROVED_SELLERS, OrderCreate, SellerCreate


@pytest.mark.parametrize("invalid_cpf", ("459452147888", "459.452.147.888", "4544.452.147.88", "0123456789"))
def test_seller_create_validate_cpf_lenght(invalid_cpf, seller_create_payload):
    seller_create_payload["cpf"] = invalid_cpf

    with pytest.raises(ValidationError):
        SellerCreate(**seller_create_payload)


def test_seller_create_remove_cpf_formatation(seller_create_payload):
    seller_create_payload["cpf"] = "788.555.666-88"

    seller_data = SellerCreate(**seller_create_payload)

    assert seller_data.cpf == "78855566688"


@pytest.mark.parametrize(
    "invalid_email",
    ("@gmail.com", "test.gmail.com", "test@gmail", "test@.com", "testgmail.com", "testgmailcom"),
)
def test_seller_create_validate_email_format(invalid_email, seller_create_payload):
    seller_create_payload["email"] = invalid_email

    with pytest.raises(ValidationError):
        SellerCreate(**seller_create_payload)


@pytest.mark.parametrize("invalid_cpf", ("459452147888", "459.452.147.888", "4544.452.147.88", "0123456789"))
def test_order_create_validate_cpf_lenght(invalid_cpf, order_create_payload):
    order_create_payload["cpf"] = invalid_cpf

    with pytest.raises(ValidationError):
        OrderCreate(**order_create_payload)


def test_order_create_remove_cpf_formatation(order_create_payload):
    order_create_payload["cpf"] = "788.555.666-88"

    order_data = OrderCreate(**order_create_payload)

    assert order_data.cpf == "78855566688"


def test_order_create_to_db_formatation(order_create_payload):
    order = OrderCreate(**order_create_payload)
    order_db_data = order.to_db()

    assert order_db_data["code"] == order_create_payload["code"]
    assert order_db_data["timestamp"].isoformat() == order_create_payload["timestamp"]
    assert order_db_data["cpf"] == order_create_payload["cpf"]
    assert str(order_db_data["amount"]) == str(order_create_payload["amount"])
    assert "status" in order_db_data
    assert "cashback_percentage" in order_db_data
    assert "cashback_amount" in order_db_data


def test_order_create_to_db_status_with_common_seller(order_create_payload):
    order = OrderCreate(**order_create_payload)
    order_db_data = order.to_db()

    assert order_db_data["status"] == "Em validação"


def test_order_create_to_db_status_with_self_approved_seller(order_create_payload):
    order_create_payload["cpf"] = ORDER_SELF_APPROVED_SELLERS[0]
    order = OrderCreate(**order_create_payload)
    order_db_data = order.to_db()

    assert order_db_data["status"] == "Aprovado"


@pytest.mark.parametrize(
    "amount, expected_percentage",
    (("10.00", 10), ("999.00", 10), ("1000.00", 15), ("1499.00", 15), ("1500", 20), ("9999999", 20),),
)
def test_order_create_to_db_cashback_calculation(amount, expected_percentage, order_create_payload):
    order_create_payload["amount"] = amount
    order = OrderCreate(**order_create_payload)
    order_db_data = order.to_db()

    expected_amount = "{:.2f}".format(expected_percentage * Decimal(amount) / 100)

    assert order_db_data["cashback_percentage"] == expected_percentage
    assert order_db_data["cashback_amount"] == expected_amount
