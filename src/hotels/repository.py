from database import Base, async_session_maker
from hotels.models import Hotel, Room
from repository.base import BaseRepo

from sqlalchemy import select

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

    @classmethod
    async def get_rooms_by_id_hotel(cls, id: int) -> Optional[ModelType]:
        async with async_session_maker() as session:
            result = await session.execute(select(cls.model).where(cls.model.hotel_id == id))
            return result.scalars().all()