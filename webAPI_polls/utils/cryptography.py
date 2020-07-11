from cryptography.fernet import Fernet

key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='

def encrypt(string):
    secret = Fernet(key)
    return secret.encrypt(string)

def decrypt(string):
    secret = Fernet(key)
    return secret.decrypt(string)

