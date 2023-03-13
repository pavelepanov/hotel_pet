from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Hotel(Base):
    __tablename__ = "hotel"

    id = Column(Integer, primary_key=True)
    name = Column(String(140), nullable=False)
    category_id = Column(Integer, ForeignKey("hotel_category.id"), nullable=False)
    location = Column(String(140), nullable=False)
    services = Column(JSON, nullable=False)
    rooms_quantity = Column(Integer, nullable=False) # Бронирование. Сумма номеров
    images_id = Column(JSON, nullable=False)
    hotel_category = relationship("HotelCategory")


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


class HotelCategory(Base):
    __tablename__ = "hotel_category"

    id = Column(Integer, primary_key=True)
    name = Column(String(140), nullable=False)