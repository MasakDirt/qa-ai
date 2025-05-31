from typing import Callable

from api.v1.schemas.fag import FAGResponseSchema
from src.orm.models import FAG

FAQTransformAllCallback = Callable[[list[FAG]], list[FAGResponseSchema]]
FAQTransformCallback = Callable[[FAG], FAGResponseSchema]
