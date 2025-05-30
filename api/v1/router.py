from fastapi import APIRouter, FastAPI
from endpoints import health


def default_router(app: FastAPI) -> None:
    router = APIRouter(prefix="/api/qa/v1")

    router.include_router(health.router, tags=["health"])

    app.include_router(router)
