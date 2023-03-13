from typing import List

from fastapi import APIRouter

from bookings.repository import RepositoryBooking

from datetime import date

from bookings.shemas import Booking


router = APIRouter(
    prefix="/booking",
)


@router.post("/{user_id}/{room_id}/{date_from}/{date_to}/{price}")
async def post_booking(id: int, user_id: int, room_id: int, date_from: date, date_to: date, price: int):
    await RepositoryBooking.add_book(id, user_id, room_id, date_from, date_to, price)