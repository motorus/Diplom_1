from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock

class TestBurger:
    def setup_method(self):
        self.burger = Burger()

    def test_set_buns_success(self):
        """Проверка метода set_buns"""
        bun_name = "Bun_name"
        bun = Bun(bun_name, 123.45)
        self.burger.set_buns(bun)
        assert self.burger.bun.get_name() == bun_name

    def test_add_ingredient_success(self):
        """Проверка метода add_ingredient"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "ingredient_name", 123.45)
        self.burger.add_ingredient(ingredient)
        self.burger.add_ingredient(ingredient)

        assert len(self.burger.ingredients) == 2

    def test_remove_ingredient_success(self):
        """Проверка метода remove_ingredient"""
        # Добавляем 4 ингридиента в бургер
        for i in range(4):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE + str(i), "ingredient_name_" + str(i), 0)
            self.burger.add_ingredient(ingredient)
        self.burger.remove_ingredient(2)  # удаляем ингредиент номер 2

        assert len(self.burger.ingredients) == 3  # проверяем что ингредиентов осталось 3
        assert self.burger.ingredients[0].get_name() == "ingredient_name_0"
        # проверяем что удалился нужный. Теперь под этим индексом другой ингредиент
        assert self.burger.ingredients[2].get_name() == "ingredient_name_3"

    def test_remove_ingredient_failed(self):
        """Проверка метода remove_ingredient с несуществующим индексом"""
        error = ""
        try:
            self.burger.remove_ingredient(1)
        except IndexError:
            error = "IndexError"

        assert error == "IndexError"

    def test_move_ingredient_success(self):
        """Проверка метода move_ingredient"""
        # Добавляем 2 ингридиента в бургер
        for i in range(2):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "ingredient_name_" + str(i), 0)
            self.burger.add_ingredient(ingredient)

        # добавим мок ингредиент
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 100
        mock_ingredient.get_name.return_value = 'sauce'
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        self.burger.add_ingredient(mock_ingredient)

        self.burger.move_ingredient(1, 2)

        # проверяем что ингредиеты с индексами 1 и 2 поменялись местами
        assert self.burger.ingredients[1].get_name() == "sauce"
        assert self.burger.ingredients[2].get_name() == "ingredient_name_1"

    def test_get_price_success(self):
        """Проверка метода get_price"""
        bun = Bun("Bun_name", 1)
        self.burger.set_buns(bun)
        # Добавляем 4 ингридиента в бургер
        for i in range(4):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "ingredient_name_" + str(i), i * 2)
            self.burger.add_ingredient(ingredient)

        assert self.burger.get_price() == 14

    def test_get_receipt_success(self):
        """Проверка метода get_receipt"""
        bun_name = "Bun_name"
        bun = Bun(bun_name, 1)
        self.burger.set_buns(bun)
        # Добавляем 4 ингридиента в бургер
        for i in range(4):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE + str(i), "ingredient_name_" + str(i), i * 2)
            self.burger.add_ingredient(ingredient)
        receipt = self.burger.get_receipt()

        assert bun_name in receipt
        assert "ingredient_name_3" in receipt
        assert "Price: 14" in receipt

    def teardown_method(self):
        self.burger = ""
