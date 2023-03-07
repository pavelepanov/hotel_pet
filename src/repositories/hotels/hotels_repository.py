from hotels.models import Hotel as HotelModel


class HotelRepository:
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