from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    """
    Тестирование функциональности класса Database.
    Проверяет корректность работы с базой данных:
    - Инициализация и наполнение данными
    - Получение списков доступных булочек и ингредиентов
    - Проверка типов и наполненности возвращаемых данных
    """

    def test_available_buns_correct_data_return_non_empty_list(self):
        """
        Проверяет, что метод available_buns() возвращает непустой список объектов Bun
        """
        database = Database()

        buns = database.available_buns()

        assert len(buns) > 0 and all(isinstance(bun, Bun) for bun in buns)
    
    def test_available_ingredients_correct_data_return_non_empty_list(self):
        """
        Проверяет, что метод available_ingredients() возвращает непустой список объектов Ingredient
        """
        database = Database()

        ingredients = database.available_ingredients()

        assert len(ingredients) > 0 and all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

    def test_init_correct_data_lists_populated(self):
        """
        Проверяет, что при инициализации Database заполняются списки булочек и ингредиентов
        """
        database = Database()

        assert len(database.buns) > 0 and len(database.ingredients) > 0
