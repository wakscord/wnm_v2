import math

from app.domain.task.repository import TaskRepository
from app.domain.task.schemas import Task


class TaskService:
    def __init__(self, task_repo: TaskRepository):
        self._task_repo = task_repo

    async def add_task(self, subscribers: list[str], message: dict, active_nodes: list[str]) -> None:
        chunked_subscribers_list = self._chunk_subscribers(subscribers, nodes_len=len(active_nodes))

        for active_node, chunked_subscribers in zip(active_nodes, chunked_subscribers_list):
            task = Task(active_node, subscribers, message)
            await self._task_repo.add_task(task)

    @staticmethod
    def _chunk_subscribers(subscribers: list[str], nodes_len: int) -> list[list[str]]:
        tasks_len: int = len(subscribers)
        chunk_len: int = math.ceil(tasks_len / nodes_len)
        # fmt: off
        return [subscribers[i * chunk_len: i * chunk_len + chunk_len] for i in range(0, nodes_len)]
