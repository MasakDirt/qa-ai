from fastapi import APIRouter

ask_router = APIRouter()


@ask_router.post(path="/ask", response_model=str)
async def process_users_question():
    ...
