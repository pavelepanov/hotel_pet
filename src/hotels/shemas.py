from typing import List

from pydantic import BaseModel


class SHotel(BaseModel):
    category_id: int
    services: List[str]
    images_id: List[str]
    name: str
    id: int
    location: str
    rooms_quantity: int

    class Config:
        orm_mode = True


class SRoom(BaseModel):
    hotel_id: int
    name: str
    price: int
    quantity: int
    description: str
    id: int
    services: List[str]
    images_id: List[str]

    class Config:
        orm_mode = True

