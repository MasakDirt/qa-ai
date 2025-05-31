from uuid import UUID

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.schemas.fag import FAGResponseSchema
from src.models.fag import FagCreateRequest
from src.orm.models import FAG
from src.utils.interfaces.repository import OrmRepositoryInterface
from src.utils.types.transform_types import FAQTransformAllCallback, FAQTransformCallback


class FAGRepository(OrmRepositoryInterface):
    __model__ = FAG

    async def get_all(
        self,
        embedded_question: list[float],
        async_session: AsyncSession,
        transform: FAQTransformAllCallback,
    ) -> list[FAGResponseSchema]:
        fags = select(self.__model__)
        stmt = (fags.order_by(self.__model__.embedding.l2_distance(embedded_question)).limit(3))

        results = (await async_session.execute(stmt)).scalars().all()
        return transform(results)

    async def get_by_id(
        self,
        id: UUID,
        async_session: AsyncSession,
        transform: FAQTransformCallback
    ) -> FAGResponseSchema:
        stmt = select(self.__model__).where(self.__model__.id == id)
        result = (await async_session.execute(statement=stmt)).scalar()

        return transform(result)

    async def create(
        self,
        model: FagCreateRequest,
        async_session: AsyncSession,
        transform: FAQTransformCallback
    ) -> FAGResponseSchema:
        stmt = (
            insert(self.__model__)
            .values(model.model_dump(exclude_unset=True))
            .returning(*self.__model__.__table__.columns)
        )
        # ID
        result = (await async_session.execute(statement=stmt)).scalar()
        await async_session.commit()

        return await self.get_by_id(
            id=result,
            async_session=async_session,
            transform=transform
        )
