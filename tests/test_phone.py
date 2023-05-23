import pytest
from _pytest.python_api import raises

from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_init(phone1):
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1
    with raises(ValueError):
        phone1.number_of_sim = 0


def test_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
