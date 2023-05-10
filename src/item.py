import csv

from src.settings import CSV_FILE


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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv.
        """
        with open(CSV_FILE, encoding="windows-1251") as file:
            reader = csv.DictReader(file)
            for i in reader:
                if list(i.keys()) == ['name', 'price', 'quantity']:
                    cls(i['name'], i['price'], i['quantity'])

    @staticmethod
    def string_to_number(number: str) -> int:
        """
        Cтатический метод, возвращающий число из числа-строки.

        :return: Число в нужном нам формате.
        """
        return int(number.split(".")[0])
