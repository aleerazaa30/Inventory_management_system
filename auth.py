# auth.py
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Vendor:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def authenticate_user(username, password):
    # Here you could add logic to authenticate the user based on role
    # For simplicity, we return a basic check
    if username == "admin" and password == "admin123":
        return Admin(username, password)
    elif username == "vendor" and password == "vendor123":
        return Vendor(username, password)
    elif username == "customer" and password == "customer123":
        return Customer(username, password)
    else:
        raise ValueError("Invalid credentials")
