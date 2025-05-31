from typing import Annotated

from pydantic import Field

from backend.src.models.base import BaseEntityModel


class OpenAIEmbeddingDataModel(BaseEntityModel):
    object: Annotated[str, Field()]
    index: Annotated[int, Field()]
    embedding: Annotated[list[float], Field()]


class OpenAIUsageModel(BaseEntityModel):
    prompt_tokens: Annotated[int, Field()]
    total_tokens: Annotated[int, Field()]


class OpenAIEmbeddingModel(BaseEntityModel):
    object: Annotated[str, Field()]
    data: Annotated[list[OpenAIEmbeddingDataModel], Field()]
    model: Annotated[str, Field()]
    usage: Annotated[OpenAIUsageModel, Field()]
