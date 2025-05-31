from api.v1.schemas.fag import FAGResponseSchema
from src.orm.models import FAG


def transform_list_of_fags_into_response(fags: list[FAG]) -> list[FAGResponseSchema]:
    return [transform_fag_into_response(fag) for fag in fags]


def transform_fag_into_response(fag: FAG) -> FAGResponseSchema:
    return FAGResponseSchema.model_validate(fag)
