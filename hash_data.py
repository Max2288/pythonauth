import hashlib
salt = 'MY_SALT'.encode()
def hash(password):
    note = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return note.hex()
    