from hashlib import sha256
from Python_Advanced.Modules_Exercise.canvas import frame


def clean_screen():
    frame.delete('all')


def get_password_hash(password):
    hash_object = sha256(password.encode())
    return hash_object.hexdigest()

