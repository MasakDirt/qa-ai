from typing import Annotated, ClassVar

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from src.configs.base import BaseApplicationConfig


class PostgresConfig(BaseApplicationConfig):
    """Config for set up Postgres connection"""

    user: Annotated[str, Field(alias="USER")]
    password: Annotated[str, Field(alias="PASS")]

    db_name: Annotated[str, Field(alias="DBNAME")]
    host: Annotated[str, Field(alias="HOST")]
    post: Annotated[int, Field(alias="PORT")]

    db_uri: Annotated[str, Field(alias="DB_URI")]
    async_db_uri: Annotated[str, Field(alias="ASYNC_DB_URI")]

    model_config = SettingsConfigDict(
        env_prefix="POSTGRES_"
    )
