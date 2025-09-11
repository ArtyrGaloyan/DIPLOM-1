import pytest
from praktikum.ingredient import Ingredient
from data import INGREDIENT_SAUCE_CORRECT


class TestIngredient:
    def test_get_name_correct_data_return_correct_name(self):
        type, name, price = INGREDIENT_SAUCE_CORRECT
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_name() == name
    
    def test_get_price_correct_data_return_correct_price(self):
        type, name, price = INGREDIENT_SAUCE_CORRECT
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_price() == price

    def test_get_type_correct_data_return_correct_type(self):
        type, name, price = INGREDIENT_SAUCE_CORRECT
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_type() == type

    @pytest.mark.parametrize('type, name, price', [
            (INGREDIENT_SAUCE_CORRECT),
            (INGREDIENT_SAUCE_CORRECT[0], "", INGREDIENT_SAUCE_CORRECT[2]),
            (INGREDIENT_SAUCE_CORRECT[0], INGREDIENT_SAUCE_CORRECT[1], 0),
            (INGREDIENT_SAUCE_CORRECT[0], "", 0)
        ]
    )
    def test_init_correct_data_attributes_set_correctly(self, type, name, price):
        ingredient = Ingredient(type, name, price)

        assert ingredient.type == type and ingredient.name == name and ingredient.price == price
