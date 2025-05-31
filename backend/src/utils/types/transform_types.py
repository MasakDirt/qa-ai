from typing import Callable

from backend.api.v1.schemas.fag import FAGResponseSchema
from backend.src.orm.models import FAG

FAQTransformAllCallback = Callable[[list[FAG]], list[FAGResponseSchema]]
FAQTransformCallback = Callable[[FAG], FAGResponseSchema]
