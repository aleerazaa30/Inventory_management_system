from auth import Admin, Vendor, Customer, authenticate_user
from inventory import Inventory, Product

def main():
    # Sample users (these are already created in auth.py)
    users = {
        "admin1": Admin("admin", "123"),
        "vendor1": Vendor("vendor1", "123"),
        "customer1": Customer("customer1", "123")
    }

    # Step 1: User Login
    username = input("Username: ")
    password = input("Password: ")

    user = authenticate_user(username, password)

    if user:  # If user is authenticated
        if isinstance(user, Admin):
            inventory = Inventory()
            # Add some default products for testing
            inventory.add_product(Product("P001", "Product1", "Category1", 100, 10))
            inventory.add_product(Product("P002", "Product2", "Category2", 200, 5))

            # Admin tasks: Add, Edit, Delete, View Products
            while True:
                print("\nAdmin Menu:")
                print("1. Add Product")
                print("2. View Products")
                print("3. Remove Product")
                print("4. Exit")

                choice = input("Enter your choice: ")
                if choice == "1":
                    # Add a new product
                    product_id = input("Enter Product ID: ")
                    name = input("Enter Product Name: ")
                    category = input("Enter Product Category: ")
                    price = float(input("Enter Product Price: "))
                    stock_quantity = int(input("Enter Stock Quantity: "))
                    product = Product(product_id, name, category, price, stock_quantity)
                    inventory.add_product(product)

                elif choice == "2":
                    # View all products
                    inventory.view_inventory()

                elif choice == "3":
                    # Remove a product
                    product_id = input("Enter Product ID to remove: ")
                    inventory.remove_product(product_id)

                elif choice == "4":
                    print("Exiting...")
                    break  # Exit
                else:
                    print("Invalid choice.")

        elif isinstance(user, Vendor):
            print("\nVendor Menu:")
            # Vendor tasks: View Products (Additional functionality can be added)
            inventory = Inventory()
            inventory.view_inventory()

        elif isinstance(user, Customer):
            print("\nCustomer Menu:")
            inventory = Inventory()

            # Sample products for testing
            inventory.add_product(Product("P001", "Product1", "Category1", 100, 10))
            inventory.add_product(Product("P002", "Product2", "Category2", 200, 5))

            while True:
                print("\n1. View Products")
                print("2. Add to Cart")
                print("3. Remove from Cart")
                print("4. Checkout")
                print("5. Exit")

                choice = input("Enter your choice: ")
                if choice == "1":
                    # View all products
                    inventory.view_inventory()

                elif choice == "2":
                    product_id = input("Enter Product ID to add to cart: ")
                    product = inventory.products.get(product_id)
                    if product:
                        user.add_to_cart(product)
                    else:
                        print("Product not found.")

                elif choice == "3":
                    product_id = input("Enter Product ID to remove from cart: ")
                    product = inventory.products.get(product_id)
                    if product:
                        user.remove_from_cart(product)
                    else:
                        print("Product not found.")

                elif choice == "4":
                    # Checkout: Decrease stock and calculate amount
                    total_amount = 0
                    for item in user.cart:
                        total_amount += item.price
                        item.stock_quantity -= 1  # Decrease stock after checkout

                    print(f"Checkout successful! Total amount: Rs{total_amount}")
                    print("Updated inventory:")
                    inventory.view_inventory()
                    # Clear the cart after checkout
                    user.cart.clear()

                elif choice == "5":
                    print("Exiting...")
                    break  # Exit
                else:
                    print("Invalid choice.")
    else:
        print("Login failed. Exiting.")

if __name__ == "__main__":
    main()
