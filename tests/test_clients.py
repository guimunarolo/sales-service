from unittest import mock

import asynctest
import pytest
from sales_service.clients import CashbackClient

pytestmark = pytest.mark.asyncio


@pytest.fixture
async def async_cashback_client():
    CashbackClient._token = "TESTE123"
    CashbackClient._url = "http://test.com"
    async with CashbackClient() as client:
        yield client


@pytest.fixture
def cashback_response():
    return {
        "statusCode": 200,
        "body": {"credit": 150,},
    }


@asynctest.patch("sales_service.clients.CashbackClient.get")
async def test_cashback_client_get_cashback(get_mock, async_cashback_client, cashback_response):
    response_json_mock = mock.Mock(return_value=cashback_response)
    get_mock.return_value.json = response_json_mock

    assert await async_cashback_client.get_cashback("12345678910") == cashback_response["body"]["credit"]
    get_mock.assert_awaited_once_with("http://test.com?cpf=12345678910", headers={"token": "TESTE123"})
    response_json_mock.assert_called_once()


@asynctest.patch("sales_service.clients.CashbackClient.get")
async def test_cashback_client_get_cashback_returns_zero_with_unexpected_value(
    get_mock, async_cashback_client, cashback_response
):
    cashback_response["body"]["credit"] = "test"
    response_json_mock = mock.Mock(return_value=cashback_response)
    get_mock.return_value.json = response_json_mock

    assert await async_cashback_client.get_cashback("12345678910") == 0


@asynctest.patch("sales_service.clients.CashbackClient.get")
async def test_cashback_client_get_cashback_returns_zero_with_unexpected_response(
    get_mock, async_cashback_client, cashback_response
):
    response_json_mock = mock.Mock(return_value={})
    get_mock.return_value.json = response_json_mock

    assert await async_cashback_client.get_cashback("12345678910") == 0
