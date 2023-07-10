import abc

from redis.asyncio import Redis


class UnsubscriberRepository(abc.ABC):
    @abc.abstractmethod
    async def get_unsubscribers(self) -> set[str]:
        raise NotImplementedError


class UnsubscriberRedisRepository(UnsubscriberRepository):
    def __init__(self, session: Redis):
        self._session = session

    async def get_unsubscribers(self) -> set[str]:
        return await self._session.smembers("unsubscribers")
