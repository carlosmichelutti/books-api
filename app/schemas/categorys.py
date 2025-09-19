from pydantic import BaseModel
from typing import List

class CategoryOut(BaseModel):

    categorys: List[str]

    class Config:
        from_attributes = True
