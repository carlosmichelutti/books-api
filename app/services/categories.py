from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from models.categories import VwCategories

class NoCategoriesFoundError(Exception):

    def __init__(
        self: object
    ) -> None:

        super().__init__('No categories found.')

async def get_all_categories(session: AsyncSession) -> dict[str, List[str]]:

    result = await session.execute(
        select(
            VwCategories.category
        )
    )

    categories = result.scalars().all()
    if not categories:
        raise NoCategoriesFoundError()
    return {'categories': categories}
