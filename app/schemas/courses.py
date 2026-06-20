from pydantic import BaseModel, ConfigDict, Field



class CourseSchema(BaseModel):
    id: int
    title: str
    description: str
    avg_rating: float | None = None
    review_count: int = 0



    model_config = ConfigDict(from_attributes=True)



class CourseCreate(BaseModel):
    title: str = Field(..., description='Название')
    description: str = Field(..., description='Описание')


    
       