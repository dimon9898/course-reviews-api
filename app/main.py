import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.routers import courses, reviews
from app.core.logger import setuplogging

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    setuplogging()
    logger.info('Процесс запущен!')
    yield
    logger.info('Приостановлен!')



app = FastAPI(lifespan=lifespan)

app.include_router(courses.router)
app.include_router(reviews.router)



@app.get('/')
async def root():
    return {'message': 'FastAPI is ready!'}


