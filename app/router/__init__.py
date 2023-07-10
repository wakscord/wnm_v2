from fastapi import APIRouter, Depends, Header, status

from app.common.exceptions import APIException
from app.common.settings import settings
from app.router.node import router as node_router
from app.router.proxy import router as proxy_router
from app.router.task import router as task_router


async def verify_token(authorization: str = Header()) -> None:
    is_verified = authorization == f"Bearer {settings.API_KEY}"
    if not is_verified:
        raise APIException(code=status.HTTP_401_UNAUTHORIZED, message="토큰이 올바르지 않습니다.")


router = APIRouter(prefix="/api", dependencies=[Depends(verify_token)])
router.include_router(proxy_router)
router.include_router(node_router)
router.include_router(task_router)
