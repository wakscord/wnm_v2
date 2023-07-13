from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.common.di import AppContainer
from app.common.exceptions import APIException
from app.domain.node.service import NodeService
from app.domain.task.schemas import TaskAddRequest, TaskAddResponse
from app.domain.task.service import TaskService
from app.router.node import provide_node_service

router = APIRouter(prefix="/tasks", tags=["task"])

provide_task_service = Provide[AppContainer.task_service]


@router.post("", description="작업 등록 API", status_code=status.HTTP_201_CREATED)
@inject
async def add_task(
    request: TaskAddRequest,
    task_service: TaskService = Depends(provide_task_service),
    node_service: NodeService = Depends(provide_node_service),
) -> TaskAddResponse:
    active_nodes = await node_service.get_active_nodes()
    if not active_nodes:
        raise APIException(code=status.HTTP_409_CONFLICT, message="활성화 노드가 존재하지 않습니다.")

    await task_service.add_task(request.subscribers, request.message, active_nodes)
    return TaskAddResponse(node_servers_count=len(active_nodes))
