class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        """
        Через try-except  
            try:
                return True if 0 < quantity <= self.quantity else False
            except ValueError:
                return 'Вне диапазона'
            except TypeError:
                return 'Должно быть целое число'
        """
        return True if 0 < quantity <= self.quantity else False

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            return self.quantity - quantity
        else:
            error_message = f'Продуктов не хватает. Максимальное кол-во {self.quantity}'
            raise ValueError(error_message)

    def __hash__(self):

        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count
        return self.products

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if remove_count is None:
            del self.products[product]
            return self.products
        elif remove_count >= self.products[product]:
            del self.products[product]
            return self.products
        else:
            self.products[product] -= remove_count
            return self.products

    def clear(self):
        return self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0
        for product in self.products:
            total_price = self.products[product] * product.price
            print(f'total_price if {total_price}')
        return total_price

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product in self.products:
            if product.check_quantity(self.products[product]):
                product.buy(self.products[product])

            else:
                error_message = f'Продуктов не хватает. Максимальное кол-во {product.quantity}'
                raise ValueError(error_message)
        # self.clear()