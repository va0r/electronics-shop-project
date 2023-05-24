import csv

from src.settings import CSV_FILE


class InstantiateCSVError(Exception):
    def __init__(self, msg='Ошибка'):
        self.msg = msg

    def __str__(self):
        return self.msg


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self) -> str:
        """
        Возвращает название товара.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Проверяет, если длина наименования товара превышает 10 символов.
        """
        if len(name) <= 10:
            self.__name = name
        else:
            raise ValueError("Exception: Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path=CSV_FILE):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv.
        """
        try:
            with open(path, encoding="windows-1251") as file:
                reader = csv.DictReader(file)
                for i in reader:
                    try:
                        cls(i['name'], i['price'], i['quantity'])
                    except Exception:
                        raise InstantiateCSVError('Файл поврежден')
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {path}')

    @staticmethod
    def string_to_number(number: str) -> int:
        """
        Cтатический метод, возвращающий число из числа-строки.

        :return: Число в нужном нам формате.
        """
        return int(number.split(".")[0])

    def __add__(self, other):
        """Сложение по количеству товара"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Складывать можно только с экземплярами классов, принадлежащих Phone или Item")
