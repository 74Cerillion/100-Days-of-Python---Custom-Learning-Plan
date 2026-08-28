from product import Product

def main():

    products = {
        '100': Product("Popcorn", "100", 2, 50),
        '200': Product("Cookies", "200", 3, 100),
    }

    print(r"""
    WELCOME TO INVENTORY MANAGEMENT! WHAT ACTION/S ARE WE PERFORMING TODAY?
    """)

    while True:
        decision = input(r"""Please choose from the following by their number:
        1: Add New Product
        2: Add Stock
        3: Remove Stock
        4: Change Price
        5: Find Product
        6: Display inventory
        7: Display inventory value
        8: Remove product
        9: Finish and Exit
        Your decision: 
        """)

        try:
            decision = int(decision)
        except ValueError:
            print("Invalid Input, please select the number value.")

        if decision in range(1, 10):
            break
        else:
            print("Invalid action, please choose from the menu provided.")

    if decision == 1:
        addPName = input("New Product Name: ")
        addPSku = input("New Product's SKU: ")
        addPPrice = input("New Product's Price: ")
        addPQuantity = input("New Product's Quantity: ")

        products[addPSku] = Product(addPName, addPSku, addPPrice, addPQuantity)

        print("New Product Added:\n{}".format(products[addPSku]))

    if decision == 2:
        addStockTo = input("Product SKU: ")
        amountToAdd = int(input("Add quantity: "))
        products[addStockTo].add_stock(amountToAdd)

    if decision == 3:
        removeStockFrom = input("Product SKU: ")
        amountToRemove = int(input("Remove Quantity: "))
        products[removeStockFrom].remove_stock(amountToRemove)

if __name__ == '__main__':
    main()