from fastapi import APIRouter

from database import get_async_session
from repository.base import BaseRepo
from fastapi import Depends

from hotels.models import Hotel

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/hotels",
)


@router.get("/")
async def get_hotel_info_with_id(id: int, session: AsyncSession = Depends(get_async_session)):
    repo = BaseRepo(Hotel)
    result = await repo.get_by_id(id, session)
    return result