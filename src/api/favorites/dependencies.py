from typing import Annotated

from fastapi import Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.favorites import crud
from src.core.models import Favorite, db_helper
from src.utils.errors import NotFound


async def favorite_by_id(
    favorite_id: Annotated[int, Path],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
) -> Favorite:
    """
    Вспомогательная функция для
    получения Resume по id
    """
    favorite = await crud.get_favorite(
        session=session,
        favorite_id=favorite_id,
    )
    if favorite is not None:
        return favorite

    raise NotFound()
