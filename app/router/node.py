from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.common.di import AppContainer
from app.domain.node.schemas import NodesResponse
from app.domain.node.service import NodeService

router = APIRouter(prefix="/nodes", tags=["node"])

provide_node_service = Provide[AppContainer.node_service]


@router.get("", description="활성화 노드 서버 조회 API")
@inject
async def nodes(node_service: NodeService = Depends(provide_node_service)) -> NodesResponse:
    nodes = await node_service.get_active_nodes()
    return NodesResponse(nodes=nodes)
