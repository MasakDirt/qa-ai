from pydantic import BaseModel, ConfigDict


class BaseModelSchema(BaseModel):
    """Base model for all request and response schemas"""

    model_config = ConfigDict(
        extra="ignore",
        from_attributes=True,
    )
