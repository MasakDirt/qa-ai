from unittest.mock import AsyncMock, MagicMock
from uuid import uuid4

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.schemas.fag import FAGResponseSchema
from src.models.fag import FagCreateRequest
from src.orm.models import FAG
from src.repositories.orm.fag import FAGRepository


@pytest.fixture
def mock_session():
    return AsyncMock(spec=AsyncSession)


@pytest.fixture
def mock_transform_all():
    return MagicMock(
        return_value=[
            FAGResponseSchema(id=uuid4(), question="Q1", answer="A1"),
            FAGResponseSchema(id=uuid4(), question="Q2", answer="A2"),
        ]
    )


@pytest.fixture
def mock_transform_one():
    return MagicMock(return_value=FAGResponseSchema(id=uuid4(), question="QX", answer="AX"))


@pytest.fixture
def repository():
    return FAGRepository()


@pytest.mark.asyncio
async def test_get_all(repository, mock_session, mock_transform_all):
    fake_fag1 = FAG(id=uuid4(), question="Q1", answer="A1", embedding=[0.1, 0.2, 0.3])
    fake_fag2 = FAG(id=uuid4(), question="Q2", answer="A2", embedding=[0.1, 0.2, 0.3])

    mock_scalars = MagicMock()
    mock_scalars.all.return_value = [fake_fag1, fake_fag2]

    mock_result = MagicMock()
    mock_result.scalars.return_value = mock_scalars

    mock_session.execute.return_value = mock_result

    result = await repository.get_all(
        embedded_question=[0.1, 0.2, 0.3],
        async_session=mock_session,
        transform=mock_transform_all
    )

    mock_session.execute.assert_awaited_once()
    mock_transform_all.assert_called_once()
    assert isinstance(result, list)
    assert all(isinstance(f, FAGResponseSchema) for f in result)


@pytest.mark.asyncio
async def test_get_by_id(repository, mock_session, mock_transform_one):
    fake_id = uuid4()
    fake_fag = FAG(id=fake_id, question="What?", answer="Answer", embedding=[0.1, 0.2, 0.3])

    mock_result = AsyncMock()
    mock_result.scalar.return_value = fake_fag
    mock_session.execute.return_value = mock_result

    result = await repository.get_by_id(
        id=fake_id,
        async_session=mock_session,
        transform=mock_transform_one
    )

    mock_session.execute.assert_awaited_once()
    mock_transform_one.assert_called_once()
    assert isinstance(result, FAGResponseSchema)


@pytest.mark.asyncio
async def test_create_calls_get_by_id(repository, mock_session, mock_transform_one):
    new_id = uuid4()
    model = FagCreateRequest(id=new_id, question="Q", answer="A", embedding=[0.1, 0.2, 0.3])

    insert_result = AsyncMock()
    insert_result.scalar.return_value = new_id

    fag_object = FAG(id=new_id, question="Q", answer="A", embedding=model.embedding)
    get_result = AsyncMock()
    get_result.scalar.return_value = fag_object

    mock_session.execute.side_effect = [insert_result, get_result]

    result = await repository.create(
        model=model,
        async_session=mock_session,
        transform=mock_transform_one
    )

    assert mock_session.execute.call_count == 2
    mock_session.commit.assert_awaited_once()
    mock_transform_one.assert_called_once()
    assert isinstance(result, FAGResponseSchema)
