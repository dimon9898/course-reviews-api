
from app.exceptions.base_exc import AppError




class ReviewNotFound(AppError):
    def __init__(self):
        self.message = 'Отзыв не найден'
        super().__init__(self.message)


class ReviewUpdateFailed(AppError):
    def __init__(self):
        self.message = 'Ошибка при редактировании отзыва'
        super().__init__(self.message)        