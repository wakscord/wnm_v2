import abc

from redis.asyncio import Redis


class ProxyRepository(abc.ABC):
    @abc.abstractmethod
    async def get_proxies(self) -> list[tuple[str, float]]:
        raise NotImplementedError

    @abc.abstractmethod
    async def add_proxy(self, proxy: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def add_proxies(self, proxies: list[str]) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete_proxy(self, proxy: str) -> None:
        raise NotImplementedError


class ProxyRedisRepository(ProxyRepository):
    _PROXIES_KEY = "proxies"

    def __init__(self, session: Redis):
        self._session = session

    async def get_proxies(self) -> list[tuple[str, float]]:
        return await self._session.zrange(self._PROXIES_KEY, start=0, end=-1, withscores=True)

    async def add_proxy(self, proxy: str) -> None:
        await self._session.zadd(self._PROXIES_KEY, mapping={proxy: 0})

    async def add_proxies(self, proxies: list[str]) -> None:
        await self._session.zadd(self._PROXIES_KEY, mapping={proxy: 0 for proxy in proxies})

    async def delete_proxy(self, proxy: str) -> None:
        await self._session.zrem(self._PROXIES_KEY, proxy)
