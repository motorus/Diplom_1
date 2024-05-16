import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def setup_method(self):
        self.database = Database()

    @pytest.mark.parametrize("index, bun_name, price", [[0, "black bun", 100],
                                                        [1, "white bun", 200],
                                                        [2, "red bun", 300]
                                                        ])
    def test_available_buns_success(self, index, bun_name, price):
        """Проверка метода available_buns"""
        assert bun_name == self.database.available_buns()[index].get_name()

    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, price",
                             [[0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
                              [1, INGREDIENT_TYPE_SAUCE, "sour cream", 200],
                              [2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
                              [3, INGREDIENT_TYPE_FILLING, "cutlet", 100],
                              [4, INGREDIENT_TYPE_FILLING, "dinosaur", 200],
                              [5, INGREDIENT_TYPE_FILLING, "sausage", 300],
                              ])
    def test_available_ingredients_success(self, index, ingredient_type, ingredient_name, price):
        """Проверка метода available_ingredients"""
        assert ingredient_name == self.database.available_ingredients()[index].get_name()

    def teardown_method(self):
        self.database = ""
