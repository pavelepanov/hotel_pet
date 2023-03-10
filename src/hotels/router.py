from typing import List

from fastapi import APIRouter

from hotels.repository import RepositoryHotels, RepositoryRooms

from hotels.shemas import SHotel, SRoom

from datetime import date


router = APIRouter(
    prefix="/hotels",
)


@router.get("/{location}", response_model=List[SHotel])
async def get_all_hotels_with_date_from_to_location(location: str):
    result = await RepositoryHotels.get_hotels_by_location(location)
    return result


@router.get("/{id}", response_model=List[SHotel])
async def get_hotel_info_with_id(id: int):
    result = await RepositoryHotels.get_by_id(id)
    return result


@router.get("/{id}/rooms", response_model=List[SRoom])
async def get_rooms_by_hotel(id: int):
    result = await RepositoryRooms.get_rooms_by_id_hotel(id)
    return result


@router.get("/{hotel_id}/{date_from}/{date_to}")
async def get_rooms_by_hotel_dateto_datefrom(hotel_id: int, date_from: date, date_to: date):
    result = await RepositoryRooms.get_rooms_by_hotel_dateto_datefrom(hotel_id, date_from, date_to)
    return result

