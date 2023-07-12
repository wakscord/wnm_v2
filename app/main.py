from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import ExceptionMiddleware
from starlette.responses import JSONResponse

from app.common.di import AppContainer
from app.common.exceptions import APIException
from app.router import router


def init_exception_handler(app: FastAPI) -> None:
    async def custom_exception_handler(_: Request, ex: APIException) -> JSONResponse:
        return JSONResponse(
            status_code=ex.code,
            content={"code": ex.code, "message": ex.message},
        )

    app.add_exception_handler(APIException, custom_exception_handler)


def init_middlewares(app: FastAPI) -> None:
    app.add_middleware(ExceptionMiddleware, handlers=app.exception_handlers)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def init_di() -> None:
    container = AppContainer()
    routers = ["proxy", "node", "task", "unsubscriber"]
    container.wire(modules=[f"app.router.{router}" for router in routers])


def create_app() -> FastAPI:
    app = FastAPI(title="WNM API", docs_url=None, description="Wakscord Node Manager")
    app.include_router(router)

    init_exception_handler(app=app)
    init_middlewares(app=app)
    init_di()

    return app


app = create_app()
