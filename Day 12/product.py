class Product:
    def __init__(self, name, sku, price, quantity):
        self.name = name
        self.sku = sku #PK | Must be unique
        self.price = price
        self.quantity = quantity