class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, product_name, quantity, price):
        self.products[product_name] = [quantity, price]

    def display_products(self):
        if not self.products:
            print("No products available in the shop.")
            return
        print("Available products in the shop:")
        for product_name, (quantity, price) in self.products.items():
            print(f"{product_name}: Quantity = {quantity}, Price = Rs {price:.2f}")


class Cart:
    def __init__(self):
        self.cart = {}

    def add_product(self, product_name, quantity):
        if product_name in self.cart:
            self.cart[product_name] += quantity
        else:
            self.cart[product_name] = quantity  

    def remove_product(self, product_name):
        if product_name in self.cart:
            del self.cart[product_name]  
            print(f"{product_name} has been removed from the cart.")
        else:
            print(f"{product_name} not found in the cart.")

    def display_cart(self):
        if not self.cart:
            print("The cart is empty.")
        else:
            print("Cart contents:")
            for product_name, quantity in self.cart.items():
                print(f"{product_name}: Quantity = {quantity}")


def main():
    shop = Shop()
    cart = Cart()

    n = int(input("Enter the number of products you want to add to the shop: "))
    for _ in range(n):
        product_name = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price: "))
        shop.add_product(product_name, quantity, price)

    while True:
        print("_________________________________")
        print("Tasks:") 
        print("1. Display products in the shop")
        print("2. Display cart")
        print("3. Add products to cart")
        print("4. Remove products from cart")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            shop.display_products()
        elif choice == 2:
            cart.display_cart()
        elif choice == 3:
            product_name = input("Enter the product name to add to cart: ")
            quantity = int(input("Enter the quantity: "))
            if product_name in shop.products:
                available_quantity = shop.products[product_name][0]
                if quantity <= available_quantity:
                    cart.add_product(product_name, quantity)
                    shop.products[product_name][0] -= quantity  
                    print(f"Added {quantity} of {product_name} to the cart.")
                else:
                    print("Not enough quantity available in the shop.")
            else:
                print("Product not found in the shop.")
        elif choice == 4:
            product_name = input("Enter the product name to remove from cart: ")
            cart.remove_product(product_name)
        elif choice == 5:
            print("Thank you for Shopping...Plz visit again...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
