import abc

from redis.asyncio import Redis


class NodeRepository(abc.ABC):
    async def is_active(self, node_id: str) -> bool:
        raise NotImplementedError

    async def get_all_nodes(self) -> list[str]:
        raise NotImplementedError

    async def delete_node(self, node_id: str) -> None:
        raise NotImplementedError


class NodeRedisRepository(NodeRepository):
    _NODE_SERVERS_KEY = "node_servers"

    def __init__(self, session: Redis):
        self._session = session

    async def is_active(self, node_id: str) -> bool:
        return bool(await self._session.get(f"health_check:{node_id}"))

    async def get_all_nodes(self) -> list[str]:
        return await self._session.hkeys(self._NODE_SERVERS_KEY)

    async def delete_node(self, node_id: str) -> None:
        await self._session.hdel(self._NODE_SERVERS_KEY, node_id)
