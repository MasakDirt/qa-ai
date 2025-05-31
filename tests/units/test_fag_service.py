import pytest
from unittest.mock import AsyncMock
from uuid import UUID

from src.services.fag import FAGService
from src.clients.openai import OpenAIClient
from src.repositories.orm.fag import FAGRepository
from api.v1.schemas.fag import FagCreateRequestSchema, FAGResponseSchema


@pytest.fixture
def mock_openai_client():
    client = AsyncMock(spec=OpenAIClient)
    client.get_embedding.return_value = [0.1, 0.2, 0.3]
    client.get_response.return_value = "Mocked AI answer"
    return client


@pytest.fixture
def mock_fag_repo():
    return AsyncMock(spec=FAGRepository)


@pytest.fixture
def mock_session():
    return AsyncMock()


@pytest.fixture
def fag_service(mock_fag_repo, mock_openai_client, mock_session):
    return FAGService(
        fag_repo=mock_fag_repo,
        openai_client=mock_openai_client,
        db_session=mock_session
    )


@pytest.mark.asyncio
async def test_get_method_returns_expected_answer(fag_service, mock_fag_repo, mock_openai_client):
    question = "What is FastAPI?"

    # Prepare mocked fags
    mocked_fags = [
        FAGResponseSchema(id=UUID("11111111-1111-1111-1111-111111111111"), question=question, answer="FastAPI is a web framework."),
        FAGResponseSchema(id=UUID("22222222-2222-2222-2222-222222222222"), question="Another Q", answer="Another A")
    ]
    mock_fag_repo.get_all.return_value = mocked_fags

    result = await fag_service.get(question)

    mock_openai_client.get_embedding.assert_awaited_once_with(question)
    mock_fag_repo.get_all.assert_awaited_once()
    mock_openai_client.get_response.assert_awaited_once_with(
        question, [fag.answer for fag in mocked_fags]
    )

    assert result == "Mocked AI answer"


@pytest.mark.asyncio
async def test_create_method_creates_new_fag(fag_service, mock_fag_repo, mock_openai_client):
    request = FagCreateRequestSchema(
        question="What is Python?",
        answer="Python is a programming language."
    )

    expected_response = FAGResponseSchema(
        id=UUID("33333333-3333-3333-3333-333333333333"),
        question=request.question,
        answer=request.answer
    )
    mock_fag_repo.create.return_value = expected_response

    result = await fag_service.create(request)

    mock_openai_client.get_embedding.assert_awaited_once_with(request.question)
    mock_fag_repo.create.assert_awaited_once()

    assert isinstance(result, FAGResponseSchema)
    assert result.question == request.question
    assert result.answer == request.answer
