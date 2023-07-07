from fastapi import APIRouter

from app.router.node import router as node_router
from app.router.proxy import router as proxy_router
from app.router.task import router as task_router

router = APIRouter(prefix="/api")
router.include_router(proxy_router)
router.include_router(node_router)
router.include_router(task_router)
