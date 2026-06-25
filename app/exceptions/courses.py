
from app.exceptions.base_exc import AppError


class CourseNotFound(AppError):
    def __init__(self):
        self.message = 'Курс не существует!'
        super().__init__(self.message)



class CourseDublicateError(AppError):
    def __init__(self, title: str):
        self.message = f'Курс с названием "{title}" уже существует'
        super().__init__(self.message)
