from app.common.schemas import BaseResponse


class UnsubscribersResponse(BaseResponse):
    unsubscribers: list[str]
