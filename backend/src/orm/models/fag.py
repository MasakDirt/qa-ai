from pgvector.sqlalchemy import Vector
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from backend.src.orm.models import BaseOrmModel

from sqlalchemy.dialects.postgresql import UUID as postgresqlUUID
from uuid import UUID as pyUUID


class FAG(BaseOrmModel):
    __tablename__ = "fag"

    id: Mapped[pyUUID] = mapped_column(postgresqlUUID, primary_key=True)
    question: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    answer: Mapped[str] = mapped_column(String(255), nullable=False)
    embedding: Mapped[list[float]] = mapped_column(Vector(1536))
