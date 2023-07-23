import abc

from redis.asyncio import Redis


class UnsubscriberRepository(abc.ABC):
    _UNSUBSCRIBERS_KEY = "unsubscribers"

    @abc.abstractmethod
    async def get_unsubscribers(self) -> set[str]:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete_all_unsubscribers(self) -> int:
        raise NotImplementedError


class UnsubscriberRedisRepository(UnsubscriberRepository):
    def __init__(self, session: Redis):
        self._session = session

    async def get_unsubscribers(self) -> set[str]:
        return await self._session.smembers(self._UNSUBSCRIBERS_KEY)

    async def delete_all_unsubscribers(self) -> int:
        deleted_count = await self._session.scard(self._UNSUBSCRIBERS_KEY)
        await self._session.delete(self._UNSUBSCRIBERS_KEY)
        return deleted_count
