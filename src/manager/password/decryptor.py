"""Password decoding and retrieval."""

import base64

from cryptography.fernet import Fernet


class Decryptor:

    def __init__(self, key: bytes | str):
        if not key:
            raise TypeError("You must provide a key to use.")
        if isinstance(key, str):
            code = key.encode("utf-8")
            self.key = base64.urlsafe_b64encode(code.ljust(32)[:32])
        elif isinstance(key, bytes):
            self.key = key

    def decrypt(self, token: bytes):
        f = Fernet(self.key)
        decoding = f.decrypt(token).decode("utf-8")
        return decoding
