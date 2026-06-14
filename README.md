# E-commers_backend

E-Commerce Management Backend

A simple and efficient REST API backend for managing an e-commerce platform. Built with Flask, this backend handles customer management, product operations, and order processing.

✨ Features


✅ Customer Management (Create, Read, Update, Delete)
✅ Product Management (Add, View, Update, Delete)
✅ Order Processing and Tracking
✅ Input Validation for all requests
✅ Error Handling with meaningful responses
✅ RESTful API endpoints
✅ JSON request/response format


🛠️ Tech Stack


Framework: Flask
Language: Python 3.8+
Database: (Add your DB:sqlite3 etc.)
Others: Flask-SQLAlchemy, python-dotenv


📋 Prerequisites

Before you begin, make sure you have:


Python 3.8 or higher
pip (Python package manager)
Git


🚀 Installation


Clone the repository


bashgit clone https://github.com/sandeep123724/ecommerce-backend.git
cd ecommerce-backend


Create a virtual environment


bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies


bashpip install -r requirements.txt


Set up environment variables
Create a .env file in the root directory:


FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key


Run the application


bashpython app.py

The server will start at http://localhost:5000

📚 API Endpoints

Customer Endpoints

Add Customer

POST /customer
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "9876543210",
  "city": "Mumbai"
}

Response: 201 Created
{
  "message": "Customer added successfully",
  "data": {...}
}

Get All Customers

GET /customer
Response: 200 OK
[{customer objects}]

Get Customer by ID

GET /customer/<id>
Response: 200 OK
{customer object}

Update Customer

PUT /customer/<id>
Content-Type: application/json

{
  "name": "Updated Name",
  "email": "newemail@example.com"
}

Response: 200 OK

Delete Customer

DELETE /customer/<id>
Response: 200 OK
{"message": "Customer deleted successfully"}

Product Endpoints

Add Product

POST /product
Content-Type: application/json

{
  "title": "Laptop",
  "price": 50000,
  "stock": 10,
  "description": "High-performance laptop"
}

Response: 201 Created

Get All Products

GET /product
Response: 200 OK
[{product objects}]

Update Product

PUT /product/<id>

Delete Product

DELETE /product/<id>

Order Endpoints

Create Order

POST /order
Content-Type: application/json

{
  "customer_id": 1,
  "product_id": 1,
  "quantity": 2
}

Response: 201 Created

Get Orders

GET /order
GET /order/<id>

📁 Project Structure

ecommerce-backend/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (add to .gitignore)
├── .gitignore             # Git ignore file
├── README.md              # This file
├── models/
│   ├── __init__.py
│   ├── customer.py        # Customer model
│   ├── product.py         # Product model
│   └── order.py           # Order model
├── routes/
│   ├── __init__.py
│   ├── customer_routes.py # Customer endpoints
│   ├── product_routes.py  # Product endpoints
│   └── order_routes.py    # Order endpoints
├── utils/
│   ├── __init__.py
│   └── validation.py      # Validation functions
└── tests/
    └── test_api.py        # Unit tests

🔍 Validation

All endpoints include input validation:


Required fields checking
Data type validation
Email format validation
Phone number validation


Example error response:

json{
  "error": "Missing required fields",
  "missing": ["email", "phone"]
}

🧪 Testing

Run tests using:

bashpython -m pytest tests/

Or test endpoints using curl:

bashcurl -X POST http://localhost:5000/customer \
  -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john@test.com","phone":"123456","city":"NYC"}'

🔐 Security Tips


Never commit .env file to GitHub
Use strong secret keys in production
Validate all user inputs
Use HTTPS in production
Add authentication/authorization as needed
Keep dependencies updated


🐛 Error Handling

The API returns meaningful error messages:

Status CodeMeaning200OK - Request successful201Created - Resource created successfully400Bad Request - Missing or invalid data404Not Found - Resource not found500Server Error - Internal server error

📦 Requirements

See requirements.txt for all dependencies:

Flask==2.3.0
Flask-SQLAlchemy==3.0.0
python-dotenv==1.0.0

Install with:

bashpip install -r requirements.txt

🤝 Contributing


Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
