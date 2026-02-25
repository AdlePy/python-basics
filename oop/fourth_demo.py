class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"name: {self.name}, price: {self.price}"

    def __repr__(self):
        return f"product: {self.name} | {self.price}"

    def make_discount(self, discount_percent):
        """
        applies discount %
        :param discount_percent
        :return None
        """
        self.price = self.price * (100 - discount_percent) / 100


laptop = Product("ASUS Rog Stryx 2000", 2000)
print(laptop)

laptop.make_discount(10)
print(laptop)
