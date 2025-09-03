class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print(f"Item '{name}' not found in cart.")

    def total_cost(self):
        return sum(self.items.values())

    def print_cart(self):
        print("Shopping Cart Contents:")
        for name, price in self.items.items():
            print(f"- {name}: ${price:.2f}")
        print(f"Total Cost: ${self.total_cost():.2f}")

# Example usage
cart = ShoppingCart()
cart.add_item("Rice", 2.5)
cart.add_item("Bread", 1.2)
cart.print_cart()
cart.remove_item("Bread")
cart.print_cart()