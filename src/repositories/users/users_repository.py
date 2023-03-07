from users.models import User as UserModel


class UserRepository:
    def __init__(self, session):
        self.session = session

    def get(self, **kwargs):
        pass

    def add(self, id, room_id, user_id, date_from, date_to, price, total_cost, total_days):
        pass

    def upgdate(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass