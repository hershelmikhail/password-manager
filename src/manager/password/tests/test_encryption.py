"""Unit tests for encryption and storage."""

import pytest

from password import Encryptor


def test_encryptor_constructor():
    assert Encryptor().auto_generated == True
    assert Encryptor("my_key").auto_generated == False


def test_encryption_return_type():
    assert type(Encryptor().encrypt("password")[0]) == bytes
    assert type(Encryptor().encrypt("password")[1]) == bytes
    assert type(Encryptor("mykey").encrypt("password")[0]) == str
    assert type(Encryptor("mykey").encrypt("password")[1]) == bytes
