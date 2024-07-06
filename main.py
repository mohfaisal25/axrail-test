
"""
This is a simple vending machine program that allows the user to buy a product
by entering the product number and the amount of notes to buy the product.

The program will then calculate the least amount of notes needed to give the change
to the user.

@author: Moh Faisal
"""


class VendingMachine:

    def __init__(self, products, available_notes):
        self.products = products
        self.avaialable_notes = sorted(available_notes, reverse=True)
        self.is_running = True

    def run(self):
        self.print_welcome_message()

        while self.is_running:
            print("\nPlease enter the product number to buy the product or enter '0' to exit.")

            try:
                product_number = int(self.get_user_input("Enter the product number: "))
                if product_number == 0:
                    self.shutdown()
                    continue

            except Exception:
                print("\nPlease enter a valid command or product number!")
                continue

            product = self.get_product_by_number(product_number)
            if product is None:
                print("\nProduct is not available! please choose from the list of available products.")
                continue

            notes_amount = 0
            product_price = product["product_price"]
            while notes_amount < product_price:
                try:
                    notes_amount = int(self.get_user_input("Enter the amount of notes: "))
                    if notes_amount < product_price:
                        print("\nThe amount of notes is not enough to buy the product!")
                        continue
                except Exception:
                    print("\nPlease only input amount of notes with a number!")
                    continue

            least_amount_of_notes = self.get_least_amount_of_notes(product_price, notes_amount)
            total_notes = len(least_amount_of_notes)
            if total_notes == 0:
                print("\nThe amount of notes is the same as the product price, no change needed!")
            else:
                print(f"\nThe least amount of notes needed to give the change is: {total_notes}\n"
                      f"with the combination of notes: {least_amount_of_notes}")

            print("\nThank you for buying the product! Please come again!\n")

    def shutdown(self):
        self.is_running = False
        print("Thank you for coming, See you!")

    def get_user_input(self, message):
        return input(message)

    def get_product_by_number(self, product_number):
        for product in self.products:
            if product["product_number"] == product_number:
                return product

        return None

    def print_welcome_message(self):
        message = "Welcome to My Vending Machine!\n"
        message += "We have the following products available:\n\n"
        for product in self.products:
            message += f"{product['product_number']}: {product['product_name']} - ${product['product_price']}\n"

        print(message)

    # This function will calculate the least amount of notes needed to give the change to the user
    #   input: product_price: int, notes_amount: int
    #   output: list of int
    def get_least_amount_of_notes(self, product_price, notes_amount):
        result = []

        change_amount = notes_amount - product_price
        if change_amount == 0:
            return result

        for note in self.avaialable_notes:
            if change_amount >= note:
                result.append(note)

        return result


if __name__ == '__main__':
    # Update the products list with your own products
    # Each product should have a product_number, product_name, and product_price
    products = [
        {"product_number": 1, "product_name": "Coca Cola", "product_price": 2},
        {"product_number": 2, "product_name": "Pepsi", "product_price": 3},
        {"product_number": 3, "product_name": "Sprite", "product_price": 5},
        {"product_number": 4, "product_name": "Fanta", "product_price": 2},
        {"product_number": 5, "product_name": "Mountain Dew", "product_price": 10},
        {"product_number": 6, "product_name": "7up", "product_price": 13},
        {"product_number": 7, "product_name": "Mirinda", "product_price": 7},
        {"product_number": 8, "product_name": "Dr. Pepper", "product_price": 15},
        {"product_number": 9, "product_name": "Red Bull", "product_price": 20}
    ]

    # In this case I use notes denominations from USD currency system
    # You can change it to any currency system
    available_notes = [1, 2, 5, 10, 20, 50, 100]

    # Create a new vending machine object
    vending_machine = VendingMachine(products, available_notes)

    # Run the vending machine
    vending_machine.run()
