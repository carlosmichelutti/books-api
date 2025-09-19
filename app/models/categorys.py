from sqlalchemy import Column, String, Integer
from database.base import Base

class VwCategorys(Base):

    __tablename__ = 'vw_categorys'
    __table_args__ = {
        'extend_existing': True,
        'schema': 'books_api'
    }
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    category = Column(String(50), unique=False, nullable=False)
    quantity_books = Column(Integer(), unique=False, nullable=False)
