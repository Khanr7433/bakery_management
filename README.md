# Bakery Management System

This project is a Bakery Management System built with Django. It allows you to manage customers, items, transactions, and inventory efficiently.

## Features

- Customer Management
- Item Management
- Transaction Management
- Inventory Management
- Tailwind CSS for styling
- Responsive design

## Installation

1. **Clone the repository:**
```sh
   git clone https://github.com/yourusername/bakery_management.git
   cd bakery_management
```

2. **Create and activate a virtual environment:**
```sh
    python -m venv bakery_env
    bakery_env\Scripts\activate  # On Windows
```

3. **Install dependencies:**
```sh
   pip install -r requirements.txt
```

4. **Set up environment variables:**
   Create a .env file in the root directory and add the following:
```sh
   SECRET_KEY=your-secret-key
   DEBUG=True
```

5. **Apply database migrations:**
```sh
   python manage.py makemigrations
   python manage.py migrate
```

6. **Create a superuser:**
```sh
   python manage.py createsuperuser
```

7. **Collect static files:**
```sh
   python manage.py collectstatic
```

8. **Run the development server:**
```sh
   python manage.py runserver
```

## Usage
1. **Access the admin panel:**
   Navigate to http://127.0.0.1:8000/admin and log in with the superuser credentials.

2. **Manage Customers:**
   Add, update, and delete customer records.

3. **Manage Items:**
   Add, update, and delete item records.

4. **Manage Transactions:**
   Create transactions for customers, including multiple items per transaction.

5. **Manage Inventory:**
   Update inventory quantities and track item transactions.

## Models
### Customer
- `id`: Unique identifier for the customer.
- `name`: Customer name.
- `email`: Customer email address.
- `phone`: Customer phone number.
- `address`: Customer address.

### Item
- `id`: Unique identifier for the item.
- `name`: Item name.
- `price`: Item price.
- `quantity`: Item quantity in stock.
- `description`: Item description.
- `category`: Item category.

### Transaction
- `id`: Unique identifier for the transaction.
- `customer`: Foreign key referencing the Customer model.
- `items`: Many-to-many relationship with the Item model.
- `total_amount`: Transaction total amount.
- `date`: Date of the transaction.

### Inventory
- `id`: Unique identifier for the inventory entry.
- `item`: Foreign key referencing the Item model.
- `quantity`: Quantity of the item in stock.
- `last_updated`: Date when the inventory was last updated.

### Category
- `id`: Unique identifier for the category.
- `name`: Category name.
- `description`: Category description.

## Views
### Customer View
- `index`: Display a list of all customers.
- `create`: Create a new customer.
- `show`: Display a customer's details.
- `update`: Update a customer's details.
- `destroy`: Delete a customer.

### Item View
- `index`: Display a list of all items.
- `create`: Create a new item.
- `show`: Display an item's details.
- `update`: Update an item's details.
- `destroy`: Delete an item.

### Transaction View
- `index`: Display a list of all transactions.
- `create`: Create a new transaction.
- `show`: Display a transaction's details.
- `update`: Update a transaction's details.
- `destroy`: Delete a transaction.

### Inventory View
- `index`: Display a list of all inventory entries.
- `update`: Update an inventory entry's details.