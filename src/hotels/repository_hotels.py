from database import Base
from repository.base import BaseRepo

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from typing import Optional, TypeVar

ModelType = TypeVar("ModelType", bound=Base)


class RepositoryHotels(BaseRepo):
    async def get_by_id(self, id: int, session: AsyncSession) -> Optional[ModelType]:
        result = await session.execute(select(self.model).where(self.model.id == id))
        return result.scalars().all()

    async def get_rooms_by_id_hotel(self, id: int, session: AsyncSession) -> Optional[ModelType]:
        result = await session.execute(select(self.model).where(self.model.hotel_id == id))
        return result.scalars().all()

    async def get_hotels_by_location(self, location: str, session: AsyncSession) -> Optional[ModelType]:
        result = await session.execute(select(self.model).filter(self.model.location.like(f"%{location}%")))
        return result.scalars().all()