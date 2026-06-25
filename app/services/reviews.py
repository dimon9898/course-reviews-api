from fastapi import Depends

from app.repositories.reviews import ReviewRepository
from app.repositories.courses import CourseRepository

from app.exceptions.courses import CourseNotFound
from app.exceptions.reviews import ReviewNotFound, ReviewUpdateFailed



class ReviewService:
    def __init__(self, repo: ReviewRepository = Depends(),
                 course_repo: CourseRepository = Depends()):
        self.repo = repo
        self.course_repo = course_repo


    async def _get_course_or_raise(self, course_id: int):
        course = await self.course_repo.get_course_by_id(course_id)

        if not course:
            raise CourseNotFound()
        
        return course

    async def get_reviews_from_course_service(self, course_id: int):
        await self._get_course_or_raise(course_id)

        return await self.repo.get_course_reviews(course_id)


    async def add_review_course_service(self, course_id: int, rating: int, text: str):
        await self._get_course_or_raise(course_id)
        
        return await self.repo.add_review_from_course(course_id, rating, text)
    
        

    async def edit_review_service(self, review_id: int, text: str):
        review = await self.repo.get_review_by_id(review_id)

        if not review:
            raise ReviewNotFound()

        is_updated = await self.repo.edit_review_from_course(review_id, text)

        if not is_updated:
            raise ReviewUpdateFailed()

        return await self.repo.get_review_by_id(review_id)