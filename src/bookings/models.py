from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date

from database import Base


class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey("room.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, nullable=False)
    total_days = Column(Integer, nullable=False)
    room = relationship("Room")
    user = relationship("User")