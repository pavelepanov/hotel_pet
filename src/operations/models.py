from sqlalchemy import Column, Integer, String, JSON, TIMESTAMP, ForeignKey, MetaData
from sqlalchemy.orm import relationship

from sqlalchemy.types import Date

from database import Base


class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey("room.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(TIMESTAMP, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, nullable=False)
    total_days = Column(Integer, nullable=False)
    room = relationship("Room")
    user = relationship("User")


class Room(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey("hotel.id"), nullable=False)
    name = Column(String(140), nullable=False)
    description = Column(String(250), nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=False)
    quantity = Column(Integer, nullable=False)
    images_id = Column(JSON, nullable=False)
    hotel = relationship("Hotel")


class Hotel(Base):
    __tablename__ = "hotel"

    id = Column(Integer, primary_key=True)
    name = Column(String(140), nullable=False)
    category_id = Column(Integer, ForeignKey("hotel_category.id"), nullable=False)
    location = Column(String(140), nullable=False)
    services = Column(JSON, nullable=False)
    rooms_quantity = Column(Integer, nullable=False)
    images_id = Column(JSON, nullable=False)
    hotel_category = relationship("HotelCategory")


class HotelCategory(Base):
    __tablename__ = "hotel_category"

    id = Column(Integer, primary_key=True)
    name = Column(String(140), nullable=False)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(140), nullable=False)
    hashed_password = Column(String(300), nullable=False)


