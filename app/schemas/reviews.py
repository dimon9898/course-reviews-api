from pydantic import BaseModel, ConfigDict, Field



class ReviewSchema(BaseModel):
    id: int
    course_id: int
    rating: int
    text: str


    model_config = ConfigDict(from_attributes=True)



class CreateReview(BaseModel):
    course_id: int = Field(..., description='ID курса', ge=1)
    rating: int = Field(..., description='Оценка (от 1 до 5)', ge=1, le=5)
    text: str = Field(..., description='Текст')



class EditReview(BaseModel):
    review_id: int = Field(..., description='ID отзыва', ge=1)
    text: str = Field(..., description='Текст')
    