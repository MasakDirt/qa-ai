from fastapi import APIRouter, FastAPI
from api.v1.endpoints import health, fag


def default_router(app: FastAPI) -> None:
    router = APIRouter(prefix="/api")

    router.include_router(health.router, tags=["health"])
    router.include_router(fag.fag_router, tags=["FAG"])

    app.include_router(router)
