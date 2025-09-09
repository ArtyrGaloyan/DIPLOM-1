from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import BUN_CORRECT, INGREDIENT_SAUCE_CORRECT


class TestBurger:
    """
    Тестирование функциональности класса Burger.
    Проверяет корректность работы с бургерами:
    - Установка булочек
    - Добавление/удаление/перемещение ингредиентов
    - Расчет общей стоимости
    - Формирование чека
    - Поведение при разных комбинациях данных
    """

    def test_set_buns_correct_data_bun_set_successfully(self, burger_empty):
        """
        Проверяет, что метод set_buns() корректно устанавливает булочку для бургера
        """
        bun = Bun(*BUN_CORRECT)

        burger_empty.set_buns(bun)

        assert burger_empty.bun and burger_empty.bun.name == bun.name and burger_empty.bun.price == bun.price

    def test_add_ingredient_correct_data_ingredient_added(self, burger_empty):
        """
        Проверяет, что метод add_ingredient() добавляет ингредиент в список ингредиентов бургера
        """
        ingredient = Ingredient(*INGREDIENT_SAUCE_CORRECT)
        
        burger_empty.add_ingredient(ingredient)
        ingredients = burger_empty.ingredients

        assert len(ingredients) == 1 and ingredients[0].name == ingredient.name and ingredients[0].type == ingredient.type and ingredients[0].price == ingredient.price

    def test_remove_ingredient_correct_data_ingredient_removed(self, burger_full):
        """
        Проверяет, что метод remove_ingredient() удаляет ингредиент из списка ингредиентов по индексу
        """
        burger_full.remove_ingredient(0)

        assert len(burger_full.ingredients) == 1

    def test_move_ingredient_correct_data_ingredient_moved(self, burger_full):
        """
        Проверяет, что метод move_ingredient() перемещает ингредиент на новую позицию в списке
        """
        ingredient_0 = burger_full.ingredients[0]

        burger_full.move_ingredient(0, 1)

        assert burger_full.ingredients[1].type == ingredient_0.type
    
    def test_get_price_correct_data_return_correct_sum(self, mocked_burger_full):
        """
        Проверяет, что метод get_price() возвращает корректную сумму цен булочки (учтённой дважды) и всех ингредиентов
        """
        manual_price = mocked_burger_full.bun.price * 2 + mocked_burger_full.ingredients[0].price

        price = mocked_burger_full.get_price()

        assert price == manual_price

    def test_get_receipt_correct_data_return_valid_receipt_lines_count(self, mocked_burger_full):
        """
        Проверяет, что метод get_receipt() возвращает чек с ожидаемым количеством строк
        """
        receipt = mocked_burger_full.get_receipt()  # 2 булки, 1 ингридиент, 2 строки на price с отступом

        assert len(receipt.split('\n')) == 5