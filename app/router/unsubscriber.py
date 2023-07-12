from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.common.di import AppContainer
from app.domain.unsubscriber.repository import UnsubscriberRepository
from app.domain.unsubscriber.schemas import UnsubscribersResponse

router = APIRouter(prefix="/unsubscribers", tags=["unsubscriber"])

provide_unsub_repository = Provide[AppContainer.unsub_repository]


@router.get("", description="구독 해지 유저 목록 조회 API")
@inject
async def unsubscribers(
    unsub_repo: UnsubscriberRepository = Depends(provide_unsub_repository),
) -> UnsubscribersResponse:
    unsubscribers = await unsub_repo.get_unsubscribers()
    return UnsubscribersResponse(unsubscribers=unsubscribers)
