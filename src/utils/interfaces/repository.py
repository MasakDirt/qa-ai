from abc import ABC, abstractmethod
from typing import Sequence

from src.orm.models import BaseOrmModel


class OrmRepositoryInterface[AbstractModel: BaseOrmModel](ABC):
    """Base ORM repository interface with CRUD operations"""

    @abstractmethod
    async def get_all(
        self, *args, **kwargs
    ) -> Sequence[AbstractModel]:
        raise NotImplementedError("Method 'get_all' is not implemented")

    @abstractmethod
    async def create(self, *args, **kwargs) -> AbstractModel:
        raise NotImplementedError("Method 'create' is not implemented")
