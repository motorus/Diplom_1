import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:
    def test_get_price_success(self):
        """Проверка метода get_price"""
        ingredient_price = 123.45
        ingredient = Ingredient("", "", ingredient_price)
        assert ingredient.get_price() == ingredient_price

    def test_get_name_success(self):
        """Проверка метода get_name"""
        ingredient_name = "some_ingredient"
        ingredient = Ingredient("", ingredient_name, 0)
        assert ingredient.get_name() == ingredient_name

    def test_get_type_success(self):
        """Проверка метода get_type"""
        ingredient_type = INGREDIENT_TYPE_SAUCE
        ingredient = Ingredient(ingredient_type, "", 0)
        assert ingredient.get_type() == ingredient_type
