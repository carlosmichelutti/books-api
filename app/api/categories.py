from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from services.categories import NoCategoriesFoundError, get_all_categories
from schemas.categories import CategoryOut
from schemas.errors import ErrorResponse
from database.session import get_session

router = APIRouter(prefix='/categories', tags=['Categories'])

@router.get(
    path='/',
    responses={
        404: {'model': ErrorResponse, 'description': 'No categories found'}
    },
    response_model=CategoryOut
)
async def get_categories_list(session: AsyncSession = Depends(get_session)):
    try:
        return await get_all_categories(session=session)
    except NoCategoriesFoundError:
        raise HTTPException(status_code=404, detail='No categories found.')
