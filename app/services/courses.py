from fastapi import Depends

from app.repositories.courses import CourseRepository
from app.exceptions.courses import CourseNotFound, CourseDublicateError





class CourseService:
    def __init__(self, repo: CourseRepository = Depends()):
        self.repo = repo


    async def get_all_course_service(self):
        return await self.repo.get_courses_with_stats()


    async def get_course_info_service(self, course_id: int):
        course = await self.repo.get_course_by_id(course_id)

        if not course:
            raise CourseNotFound()

        return course

    
    async def add_course_service(self, title: str, description: str):
        course = await self.repo.get_course_by_title(title)

        if course:
            raise CourseDublicateError(title)
        
        return await self.repo.add_course(title, description)
