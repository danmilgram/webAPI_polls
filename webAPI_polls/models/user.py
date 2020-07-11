from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, email, password, is_admin=True):
        self.id = id
        self.email = email
        self.password = password
        self.is_admin = is_admin

        users.append(self)

    def __repr__(self):
        return '<User {}>'.format(self.email)

users = []
