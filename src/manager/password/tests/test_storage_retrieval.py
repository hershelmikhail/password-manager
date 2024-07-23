"""Import sample storage and retrieval cycle."""

import pytest

from password import Decryptor, Encryptor


def test_storage_and_retrieval():
    encryptor = Encryptor()
    key, token = encryptor.encrypt("mypassword")
    decryptor = Decryptor(key)
    assert decryptor.decrypt(token) == "mypassword"

    encryptor = Encryptor("mykey")
    _, token = encryptor.encrypt("alpha1234")
    decryptor = Decryptor("mykey")
    assert decryptor.decrypt(token) == "alpha1234"
