from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from fastapi import Depends

from app.core.deps import get_db
from app.models.reviews import Review


class ReviewRepository:
    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.db = session



    async def get_course_reviews(self, course_id: int):
        result = await self.db.execute(select(Review)
                                       .where(Review.course_id == course_id)
                                       .order_by(Review.id.desc()))
        return result.scalars().all()


    async def get_review_by_id(self, review_id: int):
        result = await self.db.execute(select(Review)
                                       .where(Review.id == review_id))
        
        return result.scalar_one_or_none()


    async def add_review_from_course(self, course_id: int, rating: int, text: str):
        new_review = Review(
            course_id=course_id,
            rating=rating,
            text=text
        )

        self.db.add(new_review)
        await self.db.commit()
        await self.db.refresh(new_review)
        return new_review    
    


    async def edit_review_from_course(self, review_id: int, text: str):
        await self.db.execute(update(Review)
                              .where(Review.id == review_id).values(text=text))
        await self.db.commit()
        return True