import datetime
from datetime import date
from typing import Optional

from pydantic import BaseModel


class Booking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: datetime.timedelta

    class Config:
        orm_mode = True