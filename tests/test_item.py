import pytest
from _pytest.python_api import raises

from src.item import Item, InstantiateCSVError
from src.phone import Phone
from src.settings import CSV_FILE, CSV_FILE_ERROR


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 5000.0


def test_instantiate_from_csv():
    assert type(Item.all) is list
    Item.all.clear()
    Item.instantiate_from_csv(path=CSV_FILE)
    assert len(Item.all) == 5
    with raises(Exception):
        raise Item.instantiate_from_csv(path='error.csv') == 'Ошибка'
    with raises(Exception):
        raise Item.instantiate_from_csv(path=CSV_FILE_ERROR) == 'Файл поврежден'


def test_InstantiateCSVError():
    assert str(InstantiateCSVError()) == 'Ошибка'
    with raises(Exception):
        assert InstantiateCSVError() == 'Ошибка'


def test_string_to_number():
    assert Item.string_to_number('5.5') == 5
    with raises(Exception):
        Item.string_to_number('five')
    assert Item.string_to_number('6') == 6
    assert Item.string_to_number('9.8') == 9


def test_repr(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_name_1(item1):
    assert item1.name == "Смартфон"
    with raises(ValueError):
        item1.name = "СуперСмартфон"
    item1.name = "Яблокофон"
    assert item1.name == "Яблокофон"


def test_str(item1):
    assert str(item1) == "Смартфон"


def test__add__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item('Смартфон', 10, 3)
    assert item1 + phone1 == 8
    with raises(TypeError):
        assert item1 + 10
