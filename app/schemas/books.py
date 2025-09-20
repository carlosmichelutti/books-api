from pydantic import BaseModel

class BookOut(BaseModel):

    id: int
    title: str
    category: str
    rating: int
    price: float

    class Config:
        from_attributes = True
