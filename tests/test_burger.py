import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock


class TestBurger:

    def test_set_buns_success(self):
        """Проверка метода set_buns"""
        burger = Burger()
        bun_name = "Bun_name"
        bun = Bun(bun_name, 123.45)
        burger.set_buns(bun)
        assert burger.bun.get_name() == bun_name

    def test_add_ingredient_success(self):
        """Проверка метода add_ingredient"""
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "ingredient_name", 123.45)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 2

    def test_remove_ingredient_success(self):
        """Проверка метода remove_ingredient"""
        # Добавляем 4 ингридиента в бургер
        burger = Burger()
        for i in range(4):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE + str(i), "ingredient_name_" + str(i), 0)
            burger.add_ingredient(ingredient)
        burger.remove_ingredient(2)  # удаляем ингредиент номер 2

        assert len(burger.ingredients) == 3  # проверяем что ингредиентов осталось 3
        assert burger.ingredients[0].get_name() == "ingredient_name_0"
        # проверяем что удалился нужный. Теперь под этим индексом другой ингредиент
        assert burger.ingredients[2].get_name() == "ingredient_name_3"

    def test_move_ingredient_success(self):
        """Проверка метода move_ingredient"""
        # Добавляем 2 ингридиента в бургер
        burger = Burger()
        for i in range(2):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "ingredient_name_" + str(i), 0)
            burger.add_ingredient(ingredient)

        # добавим мок ингредиент
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 100
        mock_ingredient.get_name.return_value = 'sauce'
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(mock_ingredient)

        burger.move_ingredient(1, 2)

        # проверяем что ингредиеты с индексами 1 и 2 поменялись местами
        assert burger.ingredients[1].get_name() == "sauce"
        assert burger.ingredients[2].get_name() == "ingredient_name_1"

    def test_get_price_success(self):
        """Проверка метода get_price"""
        bun = Bun("Bun_name", 1)
        burger = Burger()
        burger.set_buns(bun)
        # Добавляем 4 ингридиента в бургер
        for i in range(4):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "ingredient_name_" + str(i), i * 2)
            burger.add_ingredient(ingredient)

        assert burger.get_price() == 14

    def test_get_receipt_success(self):
        """Проверка метода get_receipt"""
        burger = Burger()
        bun_name = "Bun_name"
        bun = Bun(bun_name, 1)
        burger.set_buns(bun)
        # Добавляем 4 ингридиента в бургер
        for i in range(4):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE + str(i), "ingredient_name_" + str(i), i * 2)
            burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        print(receipt)

        assert receipt == ('(==== Bun_name ====)\n'
                           '= sauce0 ingredient_name_0 =\n'
                           '= sauce1 ingredient_name_1 =\n'
                           '= sauce2 ingredient_name_2 =\n'
                           '= sauce3 ingredient_name_3 =\n'
                           '(==== Bun_name ====)\n'
                           '\n'
                           'Price: 14')
