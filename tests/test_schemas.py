import pytest
from pydantic import ValidationError
from sales_service.schemas import SellerCreate


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
