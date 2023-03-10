from typing import List
from urllib.request import Request

from fastapi import APIRouter

from database import get_async_session
from repository.base import BaseRepo
from fastapi import Depends

from hotels.models import Hotel, Room

from sqlalchemy.ext.asyncio import AsyncSession

from hotels.shemas import SHotel


router = APIRouter(
    prefix="/hotels",
)


@router.get("/{location}", response_model=List[SHotel])
async def get_all_hotels_with_date_from_to_location(location: str, session: AsyncSession = Depends(get_async_session)):
    repo = BaseRepo(Hotel)
    result = await repo.get_hotels_by_location(location, session)
    return result


@router.get("/{id}")
async def get_hotel_info_with_id(id: int, session: AsyncSession = Depends(get_async_session)):
    repo = BaseRepo(Hotel)
    result = await repo.get_by_id(id, session)
    return result


@router.get("/{id}/rooms")
async def get_rooms_by_hotel(id: int, session: AsyncSession = Depends(get_async_session)):
    repo = BaseRepo(Room)
    result = await repo.get_rooms_by_id_hotel(id, session)
    return result