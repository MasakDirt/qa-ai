from typing import Annotated

from pydantic import Field

from src.configs.base import BaseApplicationConfig


class OpenAIConfig(BaseApplicationConfig):
    OPENAI_API_KEY: Annotated[str, Field()]
    OPENAI_API_EMBEDDED_MODEL: Annotated[str, Field(default="text-embedding-3-small")]
    OPENAI_API_MODEL: Annotated[str, Field(default="gpt-4.1")]
