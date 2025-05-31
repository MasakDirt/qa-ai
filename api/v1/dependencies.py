from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.clients.openai import OpenAIClient
from src.repositories.orm.base import get_db
from src.repositories.orm.fag import FAGRepository
from src.services.fag import FAGService


def get_openai_client() -> OpenAIClient:
    return OpenAIClient()


def get_fag_repo() -> FAGRepository:
    return FAGRepository()


def get_fag_service(
    fag_repo: FAGRepository = Depends(get_fag_repo),
    openai_client: OpenAIClient = Depends(get_openai_client),
    session: AsyncSession = Depends(get_db)
) -> FAGService:
    return FAGService(
        fag_repo=fag_repo,
        openai_client=openai_client,
        db_session=session
    )
