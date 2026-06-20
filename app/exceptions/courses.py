

class CourseServerError(Exception):
    message: str


class CourseError(Exception):
    message: str






class CourseNotFound(CourseError):
    def __init__(self):
        self.message = 'Курс не существует!'
        super().__init__(self.message)



class CourseDublicateError(CourseError):
    def __init__(self, title: str):
        self.message = f'Курс с названием "{title}" уже существует'
        super().__init__(self.message)
