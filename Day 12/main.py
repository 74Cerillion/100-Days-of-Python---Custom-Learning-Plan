from product import Product
import sys

def main():

    products = {
        '100': Product("Popcorn", "100", 2.0, 50),
        '200': Product("Cookies", "200", 3.0, 100),
    }

    print(r"""
    WELCOME TO INVENTORY MANAGEMENT! WHAT ACTION/S ARE WE PERFORMING TODAY?
    """)

    while True:
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

        elif decision == 2:
            addStockTo = input("Product SKU: ")
            amountToAdd = int(input("Add quantity: "))
            products[addStockTo].add_stock(amountToAdd)

        elif decision == 3:
            removeStockFrom = input("Product SKU: ")
            amountToRemove = int(input("Remove Quantity: "))
            products[removeStockFrom].remove_stock(amountToRemove)

        elif decision == 4:
            changeFor = input("Product SKU: ")
            newPrice = float(input("New Price: "))
            products[changeFor].change_price(newPrice)

        elif decision == 5:
            prdName = input("Product Name: ")

            for sku, product in products.items():
                if product.name == prdName:
                    print(product)

        elif decision == 6:
            for k, v in products.items():
                print(v)

        elif decision == 7:
            totalValue = 0
            for k, v in products.items():
                itemStockWorth = v.quantity * v.price
                totalValue += itemStockWorth
            print("Total inventory value: {}.".format(totalValue))

        elif decision == 8:
            itemToDelete = input("Product SKU: ")
            for k in products.keys():
                if k == itemToDelete:
                    print("{} Removed from inventory.".format(
                        products[k].name
                        ))
                    del products[k]
                    break

        elif decision == 9:
            print("All done, See you next time!")
            sys.exit()

if __name__ == '__main__':
    main()