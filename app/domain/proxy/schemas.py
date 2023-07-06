from dataclasses import dataclass

from pydantic import BaseModel

from app.common.schemas import BaseResponse


@dataclass(frozen=True)
class ProxyInfo:
    proxy: str
    frequency: int


class ProxiesAddRequest(BaseModel):
    proxies: list[str]


class ProxiesResponse(BaseResponse):
    proxies: list[ProxyInfo]
