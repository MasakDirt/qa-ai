from typing import Annotated
from uuid import UUID

from pydantic import Field

from api.v1.schemas.base import BaseModelSchema


class FAGResponseSchema(BaseModelSchema):
    id: Annotated[UUID, Field()]
    question: Annotated[str, Field()]
    answer: Annotated[str, Field()]


class FagCreateRequestSchema(BaseModelSchema):
    question: Annotated[str, Field(min_length=1)]
    answer: Annotated[str, Field(min_length=1)]
