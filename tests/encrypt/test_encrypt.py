import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message="Olá, mundo!", key="Um")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(message=True, key=2)

    assert encrypt_message(message="ebyrT", key=10) == "Trybe"
    assert encrypt_message(message="ebyrT", key=2) == "Try_be"
    assert encrypt_message(message="yrTeb", key=3) == "Try_be"
