from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.common.di import AppContainer
from app.domain.unsubscriber.repository import UnsubscriberRepository
from app.domain.unsubscriber.schemas import DeleteAllUnsubscribersResponse, UnsubscribersResponse

router = APIRouter(prefix="/unsubscribers", tags=["unsubscriber"])

provide_unsub_repository = Provide[AppContainer.unsub_repository]


@router.get("", description="구독 해지 유저 목록 조회 API")
@inject
async def unsubscribers(
    unsub_repo: UnsubscriberRepository = Depends(provide_unsub_repository),
) -> UnsubscribersResponse:
    unsubscribers = await unsub_repo.get_unsubscribers()
    return UnsubscribersResponse(unsubscribers=unsubscribers)


@router.delete("", description="구독 해지 유저 전체 삭제 API")
@inject
async def delete_all_unsubscribers(
    unsub_repo: UnsubscriberRepository = Depends(provide_unsub_repository),
) -> DeleteAllUnsubscribersResponse:
    deleted_count = await unsub_repo.delete_all_unsubscribers()
    return DeleteAllUnsubscribersResponse(deleted_count=deleted_count)
