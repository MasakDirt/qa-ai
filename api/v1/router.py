from fastapi import APIRouter, FastAPI
from endpoints import health, ask


def default_router(app: FastAPI) -> None:
    router = APIRouter(prefix="/api")

    router.include_router(health.router, tags=["health"])
    router.include_router(ask.ask_router, tags=["ask"])

    app.include_router(router)
