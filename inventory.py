# inventory.py

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def view_inventory(self):
        if not self.products:
            print("No products in inventory.")
        for product in self.products.values():
            print(f"ID: {product.product_id}, Name: {product.name}, Price: Rs{product.price}, Stock: {product.stock_quantity}")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product with ID {product_id} removed.")
        else:
            print(f"Product with ID {product_id} not found.")
