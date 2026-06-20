from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from typing import TYPE_CHECKING

from app.models.base import Base


if TYPE_CHECKING:
    from app.models.reviews import Review


class Course(Base):
    __tablename__ = 'courses'

    title: Mapped[str] = mapped_column(String(256), index=True)
    description: Mapped[str] = mapped_column(Text)


    reviews: Mapped[list[Review]] = relationship(back_populates='course', cascade='all, delete-orphan')
