from models.database import db_connection

from sqlalchemy.orm import (
    DeclarativeBase,
    mapped_column,
    Mapped,
)

from sqlalchemy import String, Integer

class Base(DeclarativeBase):
    
    '''
        Class basis for mapping.
    '''
    pass

class Books(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, unique=True, autoincrement=True, primary_key=True)
    category: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)
    title: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    price: Mapped[str] = mapped_column(String(50), unique=False, nullable=False)
    
Base.metadata.create_all(db_connection.engine)