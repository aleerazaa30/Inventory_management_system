# Inventory_management_system
Inventory Management system designed on Python as a part of an assignment for Quarter 1 of GenAI offered by PIAIC

This project is a Web Application designed to handle user authentication and manage an inventory system. It is structured in a modular way, with distinct components responsible for handling different tasks such as user authentication (auth.py), inventory management (inventory.py), and the main application logic (main.py).

The project is designed to offer a simple yet effective solution for an inventory-based system. It integrates user authentication and allows managing products, stock levels, and more, emphasizing scalable, maintainable, and easy-to-understand code.

Modules and Functionality:

main.py:

The entry point for the application.
Manages core routes and business logic.
Acts as a coordinator between the authentication module (auth.py) and the inventory module (inventory.py).
Ensures that the necessary logic and workflows are executed based on the requests it receives (such as user authentication or inventory modifications).

auth.py:

Handles user authentication and authorization.
Manages login, user registration, and session management (typically through JWT tokens).
Ensures that only authenticated users can access specific resources (i.e., inventory management features).
Protects sensitive routes and actions by requiring users to be logged in and authorized.

inventory.py:

Handles all operations related to the inventory management system.
Manages products (add, update, delete) and stock levels (restocking, reducing inventory).
Allows users (or admins) to view product information and update inventory when necessary.
May interact with a database or another persistent storage solution to save and manage product data.

How It Works:

User Authentication:

Users must first register and log in through the auth.py module. Successful login grants a JWT token that will be used to authorize and verify user actions throughout the app.
The token is required for accessing protected routes and ensuring that only authorized users can perform sensitive operations.

Inventory Management:

Once authenticated, users can access inventory management features. These include viewing the inventory, adding new products, updating stock levels, and deleting items. All these operations are performed through the inventory.py module.
The inventory system ensures that the stock is updated in real time, and the application can be extended to integrate more advanced inventory features, such as price updates, product categorization, or tracking of sales.
Key Features:

User Authentication & Authorization:

Inventory Management:

Add, update, and delete inventory items.
View product details like name, description, price, and available stock.
Keep track of stock changes (restocks, sales, etc.).

Python: The core programming language for implementing the logic.
Project Structure:

bash
Copy code
/inventory_management_system
│
├── main.py               # Main application logic and route management.

├── auth.py               # User authentication, login, registration, and token management.

├── inventory.py          # Inventory management (products, stock, CRUD operations).

Future Enhancements:

Admin Panel: For admins to manage users, track inventory sales, and generate reports.

Notifications: Add email or SMS notifications for low stock, new product arrivals, etc.

Database Integration: Integration with a proper relational database like PostgreSQL or MySQL for better scalability and data integrity.
How to Run the Project:

Clone or download the repository to your local machine.
Run the application with python main.py
