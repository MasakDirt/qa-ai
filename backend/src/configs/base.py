from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseApplicationConfig(BaseSettings):
    """
    Base class for else application configuration

        - env_file: `.env.prod` takes priority over `.env`, also don't forget to specify path to .env
    """

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
        env_file_encoding="utf-8",
    )
