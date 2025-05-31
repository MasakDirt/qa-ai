from typing import Annotated
from uuid import UUID

from pydantic import Field

from backend.src.models.base import BaseEntityModel


class FagCreateRequest(BaseEntityModel):
    id: Annotated[UUID, Field()]
    question: Annotated[str, Field(min_length=1)]
    answer: Annotated[str, Field(min_length=1)]
    embedding: Annotated[list[float], Field(min_length=1)]
