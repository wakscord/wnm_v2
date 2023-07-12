from app.common.schemas import BaseResponse


class NodesResponse(BaseResponse):
    nodes: list[str]
