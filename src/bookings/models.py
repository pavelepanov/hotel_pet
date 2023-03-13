from sqlalchemy import Column, Integer, ForeignKey, Computed
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date

from database import Base

from users.models import User
from hotels.models import Room


class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey("room.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed("price * (date_to - date_from)")) # умножаем на колво дней
    total_days = Column(Integer, Computed("date_to - date_from"), nullable=False)
    user = relationship(User)
    room = relationship(Room)