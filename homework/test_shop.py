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
        print(e_info.value)
        assert str(e_info.value) == "'<' not supported between instances of 'int' and 'str'"
        # Через try-except
        # assert product.check_quantity('d') == 'Должно быть число'

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(10) == 990
        with pytest.raises(TypeError) as e_info:
            product.buy('someStr')
        print(e_info.value)
        assert str(e_info.value) == "'<' not supported between instances of 'int' and 'str'"

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии

        with pytest.raises(ValueError) as e_info:
            product.buy(product.quantity + 1)
        print(e_info.value)
        assert str(e_info.value) == f'Продуктов не хватает. Максимальное кол-во {product.quantity}'

        with pytest.raises(TypeError) as e_info:
            product.buy('someStr')
        print(e_info.value)
        assert str(e_info.value) == "'<' not supported between instances of 'int' and 'str'"


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_to_cart(self, product, cart):
        print(cart.add_product(product, 2))
        print()