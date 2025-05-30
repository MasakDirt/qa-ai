from fastapi import APIRouter

fag_router = APIRouter()


@fag_router.post(path="/ask", response_model=str)
async def process_users_question():
    ...
