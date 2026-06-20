from __future__ import annotations

from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Integer, ForeignKey, Text, func
from typing import TYPE_CHECKING

from app.models.base import Base


if TYPE_CHECKING:
    from app.models.courses import Course

class Review(Base):
    __tablename__ = 'reviews'

    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'))

    rating: Mapped[int] = mapped_column(Integer, nullable=False) 
    text: Mapped[str] = mapped_column(Text, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


    course: Mapped[Course] = relationship(back_populates='reviews')


