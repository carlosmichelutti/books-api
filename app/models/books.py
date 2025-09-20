from sqlalchemy import Column, String, Integer, Float, DateTime

from database.base import Base

class VwBooks(Base):

    __tablename__ = 'vw_books'
    __table_args__ = {
        'extend_existing': True,
        'schema': 'books_api'
    }
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    category = Column(String(50), unique=False, nullable=False)
    title = Column(String(200), unique=True, nullable=False)
    rating = Column(Integer, unique=False, nullable=False)
    price = Column(Float, unique=False, nullable=False)
    created_at = Column(DateTime, unique=False, nullable=False)
    updated_at = Column(DateTime, unique=False, nullable=False)

    def __repr__(self: object) -> str:
        return f'<VwBooks(id={self.id}, title={self.title})>'
