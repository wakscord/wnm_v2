from dependency_injector import containers, providers
from redis.asyncio import BlockingConnectionPool, Redis

from app.common.settings import settings
from app.domain.node.repository import NodeRedisRepository
from app.domain.node.service import NodeService
from app.domain.proxy.repository import ProxyRedisRepository
from app.domain.proxy.service import ProxyService
from app.domain.task.repository import TaskRedisRepository
from app.domain.task.service import TaskService
from app.domain.unsubscriber.repository import UnsubscriberRedisRepository


class AppContainer(containers.DeclarativeContainer):
    redis_connection_pool = providers.Resource(
        BlockingConnectionPool,
        host=settings.REDIS_URL,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASSWORD,
        decode_responses=True,
        max_connections=30,
        timeout=None,
    )
    redis_session = providers.Resource(Redis, connection_pool=redis_connection_pool)

    proxy_repository = providers.Singleton(ProxyRedisRepository, session=redis_session)
    proxy_service = providers.Singleton(ProxyService, proxy_repo=proxy_repository)

    node_repository = providers.Singleton(NodeRedisRepository, session=redis_session)
    node_service = providers.Singleton(NodeService, node_repo=node_repository)

    task_repository = providers.Singleton(TaskRedisRepository, session=redis_session)
    task_service = providers.Singleton(TaskService, task_repo=task_repository)

    unsub_repository = providers.Singleton(UnsubscriberRedisRepository, session=redis_session)
