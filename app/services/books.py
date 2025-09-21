from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from typing import List, Optional

from models.books import VwBooks

class CategoryNotFoundError(Exception):

    def __init__(
        self: object,
        category: str
    ) -> None:

        self.category: str = category

        super().__init__(f'No books found for category {category}.')

class BookNotFoundError(Exception):

    def __init__(
        self: object,
        book_id: int
    ) -> None:

        self.book_id: int = book_id

        super().__init__(f'Book with id={book_id} not found.')

async def get_books(session: AsyncSession, page: int, limit: int) -> List[VwBooks]:

    if page < 1 or limit < 1:
        raise ValueError('Page and limit must be greater than zero.') 

    result = await session.execute(
        select(
            VwBooks.id,
            VwBooks.category,
            VwBooks.title,
            VwBooks.rating,
            VwBooks.price
        ).offset(
            (page - 1) * limit
        ).limit(
            limit
        )
    )

    books = result.fetchall()
    if not books:
        raise BookNotFoundError(book_id=-1)
    return books

async def get_books_by_category(session: AsyncSession, category: str) -> List[VwBooks]:

    result = await session.execute(
        select(
            VwBooks.id,
            VwBooks.category,
            VwBooks.title,
            VwBooks.rating,
            VwBooks.price
        ).where(
            func.lower(VwBooks.category) == category.lower()
        )
    )

    books = result.fetchall()
    if not books:
        raise CategoryNotFoundError(category=category)
    return books

async def get_book_by_id(session: AsyncSession, book_id: int) -> Optional[VwBooks]:

    result = await session.execute(
        select(
            VwBooks.id,
            VwBooks.category,
            VwBooks.title,
            VwBooks.rating,
            VwBooks.price
        ).where(
            VwBooks.id == int(book_id)
        )
    )

    book = result.first()
    if not book:
        raise BookNotFoundError(book_id=book_id)
    return book
