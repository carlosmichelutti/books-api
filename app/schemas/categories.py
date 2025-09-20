from pydantic import BaseModel

class CategoryOut(BaseModel):

    categories: list[str]

    class Config:
        from_attributes = True
