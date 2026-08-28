class Product:
    def __init__(self, name, sku, price, quantity):
        self.name = name
        self.sku = sku #PK | Must be unique
        self.price = price
        self.quantity = quantity

    def __str__(self):
          return "Name: {}, SKU: {}, Price: ${}, Quantity: {}".format(
                self.name,
                self.sku,
                self.price,
                self.quantity
          )

    def add_stock(self, stock):
            self.quantity += int(stock)
            print("Total Stock for {} is now {}.".format(
                self.name, self.quantity
            ))

    def remove_stock(self, amount):
            self.quantity -= int(amount)
            print("Total Stock for {} is now {}.".format(
                self.name, self.quantity
            ))