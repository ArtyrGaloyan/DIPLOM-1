from unittest.mock import Mock
import pytest

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import BUN_CORRECT, INGREDIENT_SAUCE_CORRECT, INGREDIENT_FILLING_CORRECT

# Фабрика для создания Burger
@pytest.fixture
def burger_factory():
    def _factory(bun=None, ingredients=None):
        burger = Burger()
        if bun:
            burger.bun = bun
        if ingredients:
            burger.ingredients = ingredients
        return burger
    return _factory

# Бургер с ингредиентами и булками
@pytest.fixture
def burger_full(burger_factory):
    bun_input = Bun(*BUN_CORRECT)
    ingredients_input = [
        Ingredient(*INGREDIENT_SAUCE_CORRECT),
        Ingredient(*INGREDIENT_FILLING_CORRECT)
    ]
    return burger_factory(bun=bun_input, ingredients=ingredients_input)

# Пустой объект бургера
@pytest.fixture
def burger_empty(burger_factory):
    return burger_factory()

# Мокированный бургер (с ингредиентом и булками)
@pytest.fixture
def mocked_burger_full(burger_factory):
    # Bun mock
    mock_bun = Mock()
    mock_bun.name, mock_bun.price = BUN_CORRECT
    mock_bun.get_price.return_value = mock_bun.price
    mock_bun.get_name.return_value = mock_bun.name
    # Ingredient mock
    mock_ingredient = Mock()
    mock_ingredient.type, mock_ingredient.name, mock_ingredient.price = INGREDIENT_FILLING_CORRECT
    mock_ingredient.get_price.return_value = mock_ingredient.price
    mock_ingredient.get_name.return_value = mock_ingredient.name
    mock_ingredient.get_type.return_value = mock_ingredient.type
    # Return mocked Burger
    return burger_factory(bun=mock_bun, ingredients=[mock_ingredient])