"""Unit tests for decryption and retrieval."""

import pytest

from password import Decryptor


def test_decryption():
    assert (
        Decryptor("mykey").decrypt(
            b"gAAAAABmn82-WELDRyNLTiHxONDchMjxo8WdXuWgB3PQ7pKhEhcxAlneCioVibhke8MSo-gOxcjas0_8jgZ17MRvEiXCL8Tajg=="
        )
        == "mypassword"
    )
    assert (
        Decryptor(b"QaTJqdH4zmTbg-khA-ILPlxlLvwiAc5IcywZ9JIU4TQ=").decrypt(
            b"gAAAAABmn846Tz0z9SlWnADfq7p8eX2c7B1q6g-4M_1phfvLrrCz5QFemUFNuDWN8K2Z237D-HtYlFvoNjftsnJ9mW3_I3J-AQ=="
        )
        == "mypassword"
    )
