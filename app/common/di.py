from dependency_injector import containers, providers
from redis.asyncio import ConnectionPool, Redis

from app.common.settings import settings
from app.domain.node.repository import NodeRedisRepository
from app.domain.node.service import NodeService
from app.domain.proxy.repository import ProxyRedisRepository
from app.domain.proxy.service import ProxyService
from app.domain.task.repository import TaskRedisRepository
from app.domain.task.service import TaskService


class AppContainer(containers.DeclarativeContainer):
    redis_session = providers.Singleton(
        Redis,
        connection_pool=providers.Singleton(
            ConnectionPool, host=settings.REDIS_URL, port=6379, password=settings.REDIS_PASSWORD, decode_responses=True
        ),
    )
    proxy_repository = providers.Singleton(ProxyRedisRepository, session=redis_session)
    proxy_service = providers.Singleton(ProxyService, proxy_repo=proxy_repository)

    node_repository = providers.Singleton(NodeRedisRepository, session=redis_session)
    node_service = providers.Singleton(NodeService, node_repo=node_repository)

    task_repository = providers.Singleton(TaskRedisRepository, session=redis_session)
    task_service = providers.Singleton(TaskService, task_repo=task_repository)
