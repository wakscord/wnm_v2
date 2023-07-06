from fastapi import APIRouter

from app.router.proxy import router as proxy_router

router = APIRouter(prefix="/api")
router.include_router(proxy_router)
