from hotels.models import HotelCategory as HotelCategoryModel


class HotelCategoryRepository:
    def __init__(self, session):
        self.session = session

    def get(self, **kwargs):
        pass

    def add(self):
        pass

    def upgdate(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass