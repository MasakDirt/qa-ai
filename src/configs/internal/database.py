from typing import Annotated

from pydantic import Field

from src.configs.base import BaseApplicationConfig


class PostgresConfig(BaseApplicationConfig):
    """Config for set up Postgres connection"""

    user: Annotated[str, Field(alias="POSTGRES_USER")]
    password: Annotated[str, Field(alias="POSTGRES_PASS")]

    db_name: Annotated[str, Field(alias="POSTGRES_DBNAME")]
    host: Annotated[str, Field(alias="POSTGRES_HOST")]
    post: Annotated[int, Field(alias="POSTGRES_PORT")]

    db_uri: Annotated[str, Field(alias="POSTGRES_DB_URI")]
    async_db_uri: Annotated[str, Field(alias="POSTGRES_ASYNC_DB_URI")]
