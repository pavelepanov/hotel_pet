from typing import List

from pydantic import BaseModel


class Hotel(BaseModel):
    category_id: int
    services: List[str]
    images_id: List[str]
    name: str
    id: int
    location: str
    rooms_quantity: int

