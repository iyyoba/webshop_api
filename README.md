# Webshop API

## Project Overview

This project is a backend REST API for a webshop system. It was developed using Python and FastAPI and connects to a MariaDB database.

The API provides operations for customers, products, orders, and order items. It also uses an existing database view, database triggers, temporal data, indexes, transactions, and database user permissions.

The purpose of the project is to provide a backend service that allows applications to communicate with the webshop database through HTTP API endpoints.

## Technologies

The project uses the following technologies:

* **Python** — programming language
* **FastAPI** — web framework for building the REST API
* **Uvicorn** — ASGI server used to run the FastAPI application
* **SQLAlchemy** — ORM used to communicate with the database
* **PyMySQL** — MySQL/MariaDB database driver
* **MariaDB** — relational database management system
* **Pydantic** — data validation and API schemas
* **Swagger UI** — interactive API documentation provided by FastAPI
* **PyCharm** — development environment

## Project Structure

```text
webshop_api/
├── app/
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── customer.py
│   │   ├── product.py
│   │   ├── order.py
│   │   ├── orderitem.py
│   │   └── order_product_detail.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── customer.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── order_product_detail.py
│   │
│   └── routers/
│       ├── __init__.py
│       ├── customers.py
│       ├── products.py
│       ├── orders.py
│       ├── orderitems.py
│       └── order_product_details.py
│
├── test_database.py
├── README.md
└── .venv/
```

### Main folders

* **`app/main.py`** — starts the FastAPI application and registers the API routers.
* **`app/database.py`** — contains the database connection and SQLAlchemy session configuration.
* **`app/models/`** — contains SQLAlchemy models representing database tables and views.
* **`app/schemas/`** — contains Pydantic schemas used for API requests and responses.
* **`app/routers/`** — contains the API endpoints for each resource.
* **`test_database.py`** — simple test used to &#x76;**_**

## Database Configuration

The application uses a MariaDB database named `DB_solutions`.

The database connection is configured in:

```text
app/database.py
```

The application connects to MariaDB through SQLAlchemy and PyMySQL.

The connection uses the following structure:

```text
mysql+pymysql://username:password@localhost:3306/DB_solutions
```

The application uses the restricted database user `db_user` instead of a database administrator account. This follows the principle of least privilege because the API only needs the permissions required for normal database operations.

The database user has the following permissions:

* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`

### Database Tables

The main tables used by the API are:

* `customers`
* `products`
* `orders`
* `orderitems`
* `productcategories`

The database also contains supporting objects such as:

* `order_product_details` — database view
* `order_log` — stores order creation events
* `product_price_history` — stores product price changes
* Database triggers for logging and price history

### Security

Database passwords should not be committed to GitHub or included directly in the README. The password used by the application should be kept private and configured locally.


## Installation

### Requirements

Before running the project, install:

* Python 3.10 or newer
* MariaDB
* PyCharm or another Python IDE
* Git

### Clone the project

Clone the project from the Git repository:

```bash
git clone <repository-url>
cd webshop_api
```

Replace `<repository-url>` with the actual Git repository URL.

### Create a virtual environment

Create a Python virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment on macOS or Linux:

```bash
source .venv/bin/activate
```

### Install dependencies

Install the required Python packages:

```bash
pip install fastapi uvicorn sqlalchemy pymysql pydantic
```

The project can then be run using the virtual environment's Python interpreter.


## Configuration

Before starting the application, make sure MariaDB is running and the `DB_solutions` database is available.

Open:

```text
app/database.py
```

Configure the database connection with your local database username and password.

The connection follows this format:

```python
DATABASE_URL = (
    "mysql+pymysql://db_user:YOUR_PASSWORD"
    "@localhost:3306/DB_solutions"
)
```

Replace `YOUR_PASSWORD` with the password of the local `db_user` account.

Do not commit the real password to GitHub.

## Running the Application

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Start the FastAPI application with:

```bash
./.venv/bin/python -m uvicorn app.main:app --reload
```

When the application starts successfully, it runs locally at:

```text
http://127.0.0.1:8000
```

The `--reload` option automatically restarts the development server when Python source files are changed.

## Swagger API Documentation

FastAPI automatically provides interactive API documentation.

Open the following address in a web browser:

```text
http://127.0.0.1:8000/docs
```

The Swagger UI allows the API endpoints to be tested directly from the browser.


## API Endpoints

The API provides CRUD operations for customers, products, orders, and order items.

### Customers

Base URL:

```text
/api/customers
```

| Method | Endpoint                       | Description       |
| ------ | ------------------------------ | ----------------- |
| GET    | `/api/customers/`              | Get all customers |
| GET    | `/api/customers/{customer_id}` | Get one customer  |
| POST   | `/api/customers/`              | Create a customer |
| PUT    | `/api/customers/{customer_id}` | Update a customer |
| DELETE | `/api/customers/{customer_id}` | Delete a customer |

### Products

Base URL:

```text
/api/products
```

| Method | Endpoint                     | Description      |
| ------ | ---------------------------- | ---------------- |
| GET    | `/api/products/`             | Get all products |
| GET    | `/api/products/{product_id}` | Get one product  |
| POST   | `/api/products/`             | Create a product |
| PUT    | `/api/products/{product_id}` | Update a product |
| DELETE | `/api/products/{product_id}` | Delete a product |

### Orders

Base URL:

```text
/api/orders
```

| Method | Endpoint                 | Description                                           |
| ------ | ------------------------ | ----------------------------------------------------- |
| GET    | `/api/orders/`           | Get all orders                                        |
| GET    | `/api/orders/{order_id}` | Get one order                                         |
| POST   | `/api/orders/`           | Create an order                                       |
| PUT    | `/api/orders/{order_id}` | Update an order                                       |
| DELETE | `/api/orders/{order_id}` | Delete an order                                       |
| POST   | `/api/orders/with-item`  | Create an order and its order item in one transaction |

### Order Items

Base URL:

```text
/api/orderitems
```

| Method | Endpoint                                  | Description          |
| ------ | ----------------------------------------- | -------------------- |
| GET    | `/api/orderitems/`                        | Get all order items  |
| GET    | `/api/orderitems/{order_id}/{product_id}` | Get one order item   |
| POST   | `/api/orderitems/`                        | Create an order item |
| PUT    | `/api/orderitems/{order_id}/{product_id}` | Update an order item |
| DELETE | `/api/orderitems/{order_id}/{product_id}` | Delete an order item |

### Order Details

The order details endpoint reads data from the `order_product_details` database view.

| Method | Endpoint              | Description                                          |
| ------ | --------------------- | ---------------------------------------------------- |
| GET    | `/api/order-details/` | Get order and product details from the database view |


## Database Features

The project uses several MariaDB features in addition to the basic tables and CRUD operations.

### Database View

The project uses the `order_product_details` view.

The view combines information from several tables:

* `customers`
* `orders`
* `orderitems`
* `products`
* `productcategories`

It provides information such as:

* Customer
* Order
* Product
* Product category
* Quantity
* Unit price
* Total price

The FastAPI endpoint for this view is:

```text id="8p2zv9"
/api/order-details/
```

### Database Triggers

Two database triggers are used.

#### Order creation trigger

The `after_order_insert` trigger creates a record in the `order_log` table whenever a new order is inserted.

This provides a simple history of order creation events.

#### Product price trigger

The `product_price_update` trigger checks whether the product price has changed.

When the price changes, the trigger stores:

* Product ID
* Old price
* New price
* Change timestamp

in the `product_price_history` table.

### Temporal Data

The `product_price_history` table preserves previous product prices.

This makes it possible to see how a product's price has changed over time instead of only storing its current price.

The historical data contains:

```text
history_id
product_id
old_price
new_price
changed_at
```

### Indexes

The database uses indexes to improve query performance.

Important indexes include:

* Primary key indexes
* Foreign key indexes
* Customer first-name index
* Order date index
* Product price index

The customer first-name index was tested with `EXPLAIN`, and MariaDB used the index when searching customers by first name.

### Transactions

The API contains a transaction endpoint:

```text id="w4s9em"
/api/orders/with-item
```

This endpoint creates an order and its order item as one database transaction.

The order is first created and its generated ID is obtained. The order item is then created using that ID.

If both operations succeed, the transaction is committed.

If an error occurs, the transaction is rolled back so that the database is not left with only part of the operation completed.

### Database Security

The API connects to MariaDB using the restricted `db_user` account.

The account has:

```text id="z6r2si"
SELECT
INSERT
UPDATE
DELETE
```

permissions on the `DB_solutions` database.

The application does not need administrator-level database privileges for its normal API operations.

This follows the principle of least privilege and reduces the permissions available to the application.
