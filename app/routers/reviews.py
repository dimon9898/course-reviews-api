import logging
from fastapi import APIRouter, Depends, status, HTTPException

from app.services.reviews import ReviewService
from app.exceptions.courses import CourseNotFound
from app.exceptions.reviews import ReviewNotFound
from app.schemas.reviews import CreateReview, ReviewSchema, EditReview

logger = logging.getLogger(__name__)

router = APIRouter(prefix='/reviews', tags=['Отзывы'])


@router.get('/course/{course_id}/', response_model=list[ReviewSchema], status_code=status.HTTP_200_OK)
async def get_course_reviews(course_id: int, service: ReviewService = Depends()):
    try:
        return await service.get_reviews_from_course_service(course_id)
    
    except CourseNotFound as exc:
        logger.warning(exc.message, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=exc.message)
    except Exception as e:
        logger.error(f'Ошибка при получение отзывов курса ID={course_id}: {e}', exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Ошибка на стороне сервера')




@router.post('/add', response_model=ReviewSchema, status_code=status.HTTP_201_CREATED)
async def add_new_review_from_course(review_data: CreateReview, service: ReviewService = Depends()):
    try:
        return await service.add_review_course_service(review_data.course_id, review_data.rating, review_data.text)
    except CourseNotFound as exc:
        logger.warning(exc.message, exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=exc.message)
    except Exception as e:
        logger.error(f'Ошибка при добавление отзыва для ID={review_data.course_id}', exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Ошибка на стороне сервера')
    
    


@router.patch('/edit', status_code=status.HTTP_200_OK)
async def edit_review(review_data: EditReview, service: ReviewService = Depends()):
    try:
        return await service.edit_review_service(review_data.review_id, review_data.text)
    except ReviewNotFound as exc:
        logger.warning(f'Отзыв с ID={review_data.review_id} не найден.', exc_info=True)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=exc.message)
    except Exception as e:
        logger.error(f'Ошибка при обновление отзыва: {e}', exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Ошибка на стороне сервера')