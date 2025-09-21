from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.books import BookNotFoundError, CategoryNotFoundError, get_books, get_books_by_category, get_book_by_id
from schemas.errors import ErrorResponse
from database.session import get_session
from schemas.books import BookOut

router = APIRouter(prefix='/books', tags=['Books'])

@router.get(
    path='/',
    responses={
        400: {'model': ErrorResponse, 'description': 'Invalid request data'},
        404: {'model': ErrorResponse, 'description': 'No books found'}
    },
    response_model=list[BookOut]
)
async def get_books_data(session: AsyncSession = Depends(get_session), page: int = 1, limit: int = 50):
    try:
        return await get_books(session=session, page=page, limit=limit)
    except ValueError:
        raise HTTPException(status_code=400, detail='Page and limit must be greater than zero.')
    except BookNotFoundError:
        raise HTTPException(status_code=404, detail='No books found.')

@router.get(
    path='/{book_id}',
    responses={
        404: {'model': ErrorResponse, 'description': 'Book not found'}
    },
    response_model=BookOut
)
async def get_book_data(session: AsyncSession = Depends(get_session), book_id: int = -1):
    try:
        return await get_book_by_id(session=session, book_id=book_id)
    except BookNotFoundError:
        raise HTTPException(status_code=404, detail='Book not found.')

@router.get(
    path='/category/{category}',
    responses={
        404: {'model': ErrorResponse, 'description': 'No books found for this category'}
    },
    response_model=list[BookOut]
)
async def get_books_data_by_category(session: AsyncSession = Depends(get_session), category: str = ''):
    try:
        return await get_books_by_category(session=session, category=category)
    except CategoryNotFoundError:
        raise HTTPException(status_code=404, detail='No books found for this category.')
