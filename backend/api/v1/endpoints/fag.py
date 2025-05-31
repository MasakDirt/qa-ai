from fastapi import APIRouter, Depends

from backend.api.v1.dependencies import get_fag_service
from backend.api.v1.schemas.fag import FAGResponseSchema, FagCreateRequestSchema, FAGQuestionRequestSchema
from backend.src.services.fag import FAGService

fag_router = APIRouter()


@fag_router.post(path="/ask", response_model=str)
async def process_users_question(
    model: FAGQuestionRequestSchema,
    fag_service: FAGService = Depends(get_fag_service)
) -> str:
    return await fag_service.get(model)


@fag_router.post(path="/admin/fags", response_model=list[FAGResponseSchema])
async def create_fag(
    create_models: list[FagCreateRequestSchema],
    fag_service: FAGService = Depends(get_fag_service)
) -> list[FAGResponseSchema]:
    return [await fag_service.create(create_model) for create_model in create_models]
