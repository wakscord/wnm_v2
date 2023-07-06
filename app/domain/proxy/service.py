import dacite

from app.domain.proxy.repository import ProxyRepository
from app.domain.proxy.schemas import ProxyInfo


class ProxyService:
    def __init__(self, proxy_repo: ProxyRepository):
        self._proxy_repo = proxy_repo

    async def get_proxies(self) -> list[ProxyInfo]:
        raw_proxies = await self._proxy_repo.get_proxies()
        return [
            dacite.from_dict(data_class=ProxyInfo, data={"proxy": proxy, "frequency": int(frequency)})
            for proxy, frequency in raw_proxies
        ]

    async def add_proxy(self, proxy: str) -> None:
        await self._proxy_repo.add_proxy(proxy)

    async def add_proxies(self, proxies: list[str]) -> None:
        await self._proxy_repo.add_proxies(proxies)

    async def delete_proxy(self, proxy: str) -> None:
        await self._proxy_repo.delete_proxy(proxy)
