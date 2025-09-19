from pydantic import BaseModel
from datetime import datetime

class BookOut(BaseModel):

    id: int
    title: str
    category: str
    rating: int
    price: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
