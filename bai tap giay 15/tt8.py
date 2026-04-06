class Product:
    def __init__(self, price):
        self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Giá không thể nhỏ hơn 0!")
        self._price = value
p = Product(100)
p.price = 50
print(p.price)