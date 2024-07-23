"""Password encoding and retrieval."""

import base64

from cryptography.fernet import Fernet


class Encryptor:

    def __init__(self, key: str = None):
        if not key:
            self.key = Fernet.generate_key()
            self.auto_generated = True
        else:
            self.custom_key = key
            code = key.encode("utf-8")
            self.key = base64.urlsafe_b64encode(code.ljust(32)[:32])
            self.auto_generated = False

    def encrypt(self, password: str):
        f = Fernet(self.key)
        password_bytes = password.encode("utf-8")
        token = f.encrypt(password_bytes)
        if not self.auto_generated:
            return self.custom_key, token
        return self.key, token
