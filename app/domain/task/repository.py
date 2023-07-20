import abc

import orjson
from redis.asyncio import Redis

from app.domain.task.schemas import Task


class TaskRepository(abc.ABC):
    _NODE_TASK_QUEUE = "node_task_queue"

    @abc.abstractmethod
    async def add_task(self, task: Task) -> None:
        raise NotImplementedError


class TaskRedisRepository(TaskRepository):
    def __init__(self, session: Redis):
        self._session = session

    async def add_task(self, task: Task) -> None:
        await self._session.rpush(self._NODE_TASK_QUEUE, orjson.dumps({"keys": task.subscribers, "data": task.message}))
