class Product:
    def __init__(self, price):
        self._price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("gia phai lon hon 0")
    def __str__(self):
        return f"gia sp: {self._price}"
product = Product(36363636363636)
print(product)
product.price =57575700
print(product)