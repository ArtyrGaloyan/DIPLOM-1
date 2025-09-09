import pytest
from praktikum.bun import Bun
from data import BUN_CORRECT


class TestBun:
    """
    Тестирование функциональности класса Bun.
    Проверяет корректность работы с булочками:
    - Получение названия и цены
    - Инициализация с разными типами данных (валидные, граничные значения)
    - Сохранение атрибутов при создании объекта
    """

    def test_get_name_correct_data_return_correct_name(self):
        """
        Проверяет, что метод get_name() возвращает корректное название булочки при передаче валидных данных
        """
        name, price = BUN_CORRECT
        bun = Bun(name, price)

        assert bun.get_name() == name
    
    def test_get_price_correct_data_return_correct_price(self):
        """
        Проверяет, что метод get_price() возвращает корректную цену булочки при передаче валидных данных
        """
        name, price = BUN_CORRECT
        bun = Bun(name, price)

        assert bun.get_price() == price

    @pytest.mark.parametrize('name, price', [
            (BUN_CORRECT),
            (BUN_CORRECT[0], 0),
            ("", BUN_CORRECT[1]),
            ("", 0)
        ]
    )
    def test_init_correct_data_attributes_set_correctly(self, name, price):
        """
        Проверяет, что инициализация объекта Bun с разными типами данных (валидные, пустая строка, нулевая цена) корректно устанавливает атрибуты
        """
        bun = Bun(name, price)

        assert bun.name == name and bun.price == price
