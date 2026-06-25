from sqlalchemy import func, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.core.deps import get_db
from app.models.courses import Course
from app.models.reviews import Review
from app.schemas.courses import CourseSchema

class CourseRepository:
    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.db = session


    async def get_courses_with_stats(self):
        result = await self.db.execute(select(
                                            Course.id,
                                            Course.title,
                                            Course.description,
                                            func.coalesce(func.round(func.avg(Review.rating), 1), 0.0).label('avg_rating'),
                                            func.count(Review.id).label('review_count'))
                                        .outerjoin(Course.reviews)
                                        .group_by(Course.id))

        courses = result.all()

        return [CourseSchema.model_validate(row._asdict()) for row in courses]


    async def get_course_by_id(self, course_id: int):
        result = await self.db.execute(select(Course.id,
                                              Course.title,
                                              Course.description,
                                              func.coalesce(func.round(func.avg(Review.rating), 1), 0.0).label('avg_rating'),
                                              func.count(Review.id).label('review_count'))
                                        .outerjoin(Course.reviews)
                                        .where(Course.id == course_id)
                                        .group_by(Course.id))
        
        row = result.one_or_none()        

        if row is None:
            return None
        
        print(row._asdict())

        return CourseSchema.model_validate(row._asdict())
    

    async def get_course_by_title(self, title: str):
        result = await self.db.execute(select(Course)
                                       .where(Course.title == title.capitalize()))
        
        return result.scalar_one_or_none()


    async def add_course(self, title: str, description: str):
        new_course = Course(
            title=title.capitalize(),
            description=description
        )
        self.db.add(new_course)
        await self.db.commit()
        await self.db.refresh(new_course)

        return new_course
