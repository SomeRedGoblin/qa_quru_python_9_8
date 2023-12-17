"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False
        assert product.check_quantity(0) is False
        assert product.check_quantity(-1) is False
        with pytest.raises(TypeError) as e_info:
            product.check_quantity('someStr')
        assert str(e_info.value) == "'<' not supported between instances of 'int' and 'str'"
        # Через try-except
        # assert product.check_quantity('d') == 'Должно быть число'

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(10) == 990

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии

        with pytest.raises(ValueError) as e_info:
            product.buy(product.quantity + 1)
        assert str(e_info.value) == f'Продуктов не хватает. Максимальное кол-во {product.quantity}'

    def test_product_buy_wrong_type_data(self, product):
        with pytest.raises(TypeError) as e_info:
            product.buy('someStr')
        assert str(e_info.value) == "'<' not supported between instances of 'int' and 'str'"


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_to_cart(self, product, cart):
        cart.add_product(product, 2)
        assert cart.products[product] == 2
        cart.add_product(product, 3)
        assert cart.products[product] == 5
        cart.add_product(product, 1000)
        assert cart.products[product] == 1005

    def test_remove_from_cart(self, product, cart):
        cart.add_product(product, 2)
        cart.remove_product(product, None)
        assert (product in cart.products) is False

        cart.add_product(product, 2)
        cart.remove_product(product, 2)
        assert (product in cart.products) is False

        cart.add_product(product, 2)
        cart.remove_product(product, 3)
        assert (product in cart.products) is False

        cart.add_product(product, 5)
        cart.remove_product(product, 2)
        assert cart.products[product] == 3

    def test_clear_cart(self, product, cart):
        cart.add_product(product, 5)
        cart.clear()
        assert cart.products == {}

    def test_check_price(self, product, cart):
        cart.add_product(product, 5)
        assert cart.get_total_price() == 500

        cart.clear()
        assert cart.get_total_price() == 0

    def test_cart_buy_product(self, product, cart):
        cart.add_product(product, 10)
        cart.buy()
        assert product.quantity == 990

        cart.add_product(product, 30)
        cart.buy()
        assert product.quantity == 960

    def test_cart_buy_more_than_available(self, product, cart):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError) as e_info:
            cart.buy()
        assert str(e_info.value) == "Продуктов не хватает. Максимальное кол-во 1000"

    def test_cart_buy_another_product(self, product, cart):
        cart.add_product(product, 10)
        new_product = Product("book", 100, "This is a book", 1000)
        cart.add_product(new_product, 10)
        assert cart.products.__len__() == 1
