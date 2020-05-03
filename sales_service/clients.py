import httpx

from .configs import settings


class CashbackClient(httpx.AsyncClient):
    _token = settings.EXTERNAL_API_TOKEN
    _url = "https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback"

    async def get_cashback(self, cpf):
        response = await self.get(f"{self._url}?cpf={cpf}", headers={"token": self._token})
        data = response.json()

        try:
            return int(data["body"]["credit"])
        except (KeyError, ValueError):
            return 0
