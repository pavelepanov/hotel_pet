from repository.base import BaseRepo

from database import Base, async_session_maker

from typing import TypeVar

from bookings.models import Booking

from sqlalchemy.types import Date

from sqlalchemy import insert

from datetime import date


ModelType = TypeVar("ModelType", bound=Base)


class RepositoryBooking(BaseRepo):
    model = Booking

    @classmethod
    async def add_book(cls, id: int,  user_id: int, room_id: int,  date_from: date, date_to: date, price: int):
        async with async_session_maker() as session:
            await session.execute(
                insert(cls.model),
                [
                    {"id": id, "room_id": room_id, "user_id": user_id, "date_from": date_from, "date_to": date_to, "price": price, "total_days": date_to.day - date_from.day, "total_cost": price * (date_to.day - date_from.day)}
                ]
            )

            await session.commit()
