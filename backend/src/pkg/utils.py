import httpx


class ClientKit:
    def __init__(self):
        self.asyn_client=self.init_async_client()

    def init_async_client(self) -> httpx.AsyncClient:
            return httpx.AsyncClient()

    async def teardown_async_client(self) -> bool:
        """
        Close the async client
        """
        await self.async_client.aclose()
        return self.async_client.is_closed

httpx_kit = ClientKit()