from bookings.models import Booking as BookingModel


class BookingRepository:
    def __init__(self, session):
        self.session = session

    def get(self, **kwargs):
        pass

    def add(self, id, room_id, user_id, date_from, date_to, price, total_cost, total_days):
        booking = BookingModel(
            id = id,
            room_id = room_id,
            user_id = user_id,
            date_from = date_from,
            date_to = date_to,
            price = price,
            total_cost = total_cost,
            total_days = total_days,
        )
        self.session.add(booking)

    def upgdate(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass