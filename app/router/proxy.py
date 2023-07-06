from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.common.di import AppContainer
from app.common.schemas import BaseResponse
from app.domain.proxy.schemas import ProxiesAddRequest, ProxiesResponse
from app.domain.proxy.service import ProxyService

router = APIRouter(prefix="/proxies", tags=["proxy"])


@router.get("", description="프록시 목록 조회 API", response_model=ProxiesResponse)
@inject
async def proxies(proxy_service: ProxyService = Depends(Provide[AppContainer.proxy_service])) -> dict:
    proxies = await proxy_service.get_proxies()
    return {"proxies": proxies}


@router.post("/{proxy}", description="프록시 추가 API", status_code=201)
@inject
async def add_proxy(
    proxy: str, proxy_service: ProxyService = Depends(Provide[AppContainer.proxy_service])
) -> BaseResponse:
    await proxy_service.add_proxy(proxy)
    return BaseResponse()


@router.post("", description="프록시 벌크 추가 API", status_code=201)
@inject
async def add_proxies(
    request: ProxiesAddRequest, proxy_service: ProxyService = Depends(Provide[AppContainer.proxy_service])
) -> BaseResponse:
    await proxy_service.add_proxies(request.proxies)
    return BaseResponse()


@router.delete("/{proxy}", description="프록시 삭제 API", status_code=204)
@inject
async def delete_proxy(proxy: str, proxy_service: ProxyService = Depends(Provide[AppContainer.proxy_service])) -> None:
    await proxy_service.delete_proxy(proxy)
