from praktikum.bun import Bun


class TestBun:
    def test_get_name_success(self):
        """Проверка метода get_name"""
        test_bun_name = "Булка_1"
        test_bun_price = 0
        bun = Bun(test_bun_name, test_bun_price)
        assert bun.get_name() == test_bun_name

    def test_get_price_success(self):
        """Проверка метода get_price"""
        test_bun_name = ""
        test_bun_price = 123.45
        bun = Bun(test_bun_name, test_bun_price)
        assert bun.get_price() == test_bun_price
