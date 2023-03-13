from database import Base, async_session_maker
from hotels.models import Hotel, Room
from bookings.models import Booking
from repository.base import BaseRepo
from sqlalchemy import func

from sqlalchemy import select, and_

from typing import Optional, TypeVar

ModelType = TypeVar("ModelType", bound=Base)


class RepositoryHotels(BaseRepo):
    model = Hotel

    @classmethod
    async def get_by_id(cls, id: int) -> Optional[ModelType]:
        async with async_session_maker() as session:
            result = await session.execute(select(cls.model).where(cls.model.id == id)) # Не работает
            return result.scalars().all()

    @classmethod
    async def get_hotels_by_location(cls, location: str) -> Optional[ModelType]:
        async with async_session_maker() as session:
            result = await session.execute(select(cls.model).filter(cls.model.location.like(f"%{location}%")))
            return result.scalars().all()


class RepositoryRooms(BaseRepo):
    model = Room
    booking = Booking
    hotel = Hotel

    @classmethod
    async def get_rooms_by_id_hotel(cls, id: int) -> Optional[ModelType]:
        async with async_session_maker() as session:
            result = await session.execute(select(cls.model).where(cls.model.hotel_id == id))
            return result.scalars().all()

    @classmethod
    async def get_rooms_by_hotel_dateto_datefrom(cls, hotel_id: int) -> Optional[ModelType]:
        async with async_session_maker() as session:
            result_one = await session.execute(select(func.count(cls.model.id)).join(cls.booking, and_(cls.model.hotel_id == hotel_id, cls.booking.room_id == cls.model.id)))
            result_two = await session.execute(select(cls.hotel.rooms_quantity).where(cls.hotel.id == hotel_id))
            return result_two.scalars().all()[0] - result_one.scalars().all()[0]