import logging

from fastapi import APIRouter, Depends, status, HTTPException

from app.schemas.courses import CourseSchema, CourseCreate
from app.services.courses import CourseService
from app.exceptions.courses import CourseNotFound, CourseDublicateError




logger = logging.getLogger(__name__)
router = APIRouter(prefix='/courses', tags=['Курсы'])




@router.get('/list', response_model=list[CourseSchema], status_code=status.HTTP_200_OK)
async def get_courses(service: CourseService = Depends()):
    try:
        return await service.get_all_course_service()
    except Exception as e:
        logger.error(f'Непредвиденная ошибка при получении списка курсов: {e}', exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f'Ошибка на стороне сервера')




@router.get('/get/{course_id}', response_model=CourseSchema, status_code=status.HTTP_200_OK)
async def get_course(course_id: int, service: CourseService = Depends()):
    try:
        return await service.get_course_info_service(course_id)
    except CourseNotFound as exc:
        logger.warning(f'Курс не найден: id={course_id} — {exc.message}')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=exc.message)
    except Exception as e:
        logger.error(f'Непредвиденная ошибка при поиске курса id={course_id}: {e}', exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Ошибка на стороне сервера')
        



@router.post('/add', status_code=status.HTTP_201_CREATED)
async def add_course(course_data: CourseCreate, service: CourseService = Depends()):
    try:
        return await service.add_course_service(course_data.title, course_data.description)
    except CourseDublicateError as exc:
        logger.warning(f'Дубликат курса: "{course_data.title}" — {exc.message}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=exc.message)
    except Exception as e:
        logger.error(f'Непредвиденная ошибка при добавлении курса: {e}', exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='Ошибка на стороне сервера')


