from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models
from .customer import Customer
from .customer_account import CustomerAccount
from .product import Product
from .order import Order
