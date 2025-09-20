from sqlalchemy import Column, String, Integer

from database.base import Base

class VwCategories(Base):

    __tablename__ = 'vw_categories'
    __table_args__ = {
        'extend_existing': True,
        'schema': 'books_api'
    }
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    category = Column(String(50), unique=False, nullable=False)
    quantity_books = Column(Integer, unique=False, nullable=False)

    def __repr__(self: object) -> str:
        return f'<VwCategories(category={self.category}, quantity_books={self.quantity_books})>'
