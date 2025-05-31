from fastapi import APIRouter, Depends, Request, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from api.v1.dependencies import get_fag_service
from api.v1.schemas.fag import FAGResponseSchema, FagCreateRequestSchema
from src.services.fag import FAGService

fag_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@fag_router.get("/ask", response_class=HTMLResponse)
async def ask_page(request: Request):
    return templates.TemplateResponse("ask_form.html", {"request": request, "answer": None})


@fag_router.post("/ask", response_class=HTMLResponse)
async def process_user_question(
    request: Request,
    question: str = Form(...),
    fag_service: FAGService = Depends(get_fag_service)
):
    answer = await fag_service.get(question)
    return templates.TemplateResponse(
        "ask_form.html",
        {"request": request, "answer": answer, "question": question}
    )


@fag_router.post(path="/admin/fags", response_model=list[FAGResponseSchema])
async def create_fag(
    create_models: list[FagCreateRequestSchema],
    fag_service: FAGService = Depends(get_fag_service)
) -> list[FAGResponseSchema]:
    return [await fag_service.create(create_model) for create_model in create_models]
