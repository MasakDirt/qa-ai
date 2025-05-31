from uuid import uuid4, UUID

from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.schemas.fag import FAGResponseSchema, FAGQuestionRequestSchema, FagCreateRequestSchema
from src.clients.openai import OpenAIClient
from src.models.fag import FagCreateRequest
from src.repositories.orm.fag import FAGRepository
from src.services.base import BaseService
from src.utils.transforms.database import transform_list_of_fags_into_response, transform_fag_into_response


class FAGService(BaseService):
    def __init__(self, fag_repo: FAGRepository, openai_client: OpenAIClient, db_session: AsyncSession):
        self._fag_repo = fag_repo
        self._openai_client = openai_client
        self._session = db_session

    async def get(self, request: FAGQuestionRequestSchema) -> str:
        logger.debug(f"Getting fag`s for question: {request.question}")
        embedded_question = await self._openai_client.get_embedding(request.question)

        fags = await self._fag_repo.get_all(
            embedded_question=embedded_question,
            async_session=self._session,
            transform=transform_list_of_fags_into_response
        )

        return await self._openai_client.get_response(request.question, [fag.answer for fag in fags])

    async def create(self, create_model: FagCreateRequestSchema) -> FAGResponseSchema:
        embedding = await self._openai_client.get_embedding(create_model.question)

        fag = await self._fag_repo.create(
            async_session=self._session,
            transform=transform_fag_into_response,
            model=FagCreateRequest(
                id=uuid4(),
                question=create_model.question,
                answer=create_model.answer,
                embedding=embedding
            )
        )
        logger.info(f"Created new fag for question: {create_model.question}")
        return fag
