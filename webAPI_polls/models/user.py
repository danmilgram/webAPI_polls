from cryptography.fernet import Fernet
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='

class User(UserMixin):
    def __init__(self, id, email, password, is_admin=True):
        self.id = id
        self.email = email
        self.password = password
        self.is_admin = is_admin

        users.append(self)

    def __repr__(self):
        return '<User {}>'.format(self.email)

def encryptPass(password):
    secret = Fernet(key)
    return secret.encrypt(password)

def decryptPass(password):
    secret = Fernet(key)
    return secret.decrypt(password)

users = []
