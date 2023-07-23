from app.common.schemas import BaseResponse


class UnsubscribersResponse(BaseResponse):
    unsubscribers: list[str]


class DeleteAllUnsubscribersResponse(BaseResponse):
    deleted_count: int
