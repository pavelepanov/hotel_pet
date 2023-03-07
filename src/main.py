from fastapi import FastAPI

from repositories.bookings.bookings_repository import BookingRepository
from repositories.hotels.hotels_repository import HotelRepository
from repositories.hotels.hotel_categories_repository import HotelCategoryRepository
from repositories.users.users_repository import UserRepository
from repositories.tools.repositories_registry import RepositoriesRegistry

app = FastAPI(
    title="Hotel project"
)


def register_repositories():
    repositories_registry_booking = RepositoriesRegistry(repo=BookingRepository)
    repositories_registry_hotel = RepositoriesRegistry(repo=HotelRepository)
    repositories_registry_hotel_category = RepositoriesRegistry(repo=HotelCategoryRepository)
    repositories_registry_user = RepositoriesRegistry(repo=UserRepository)


register_repositories()
