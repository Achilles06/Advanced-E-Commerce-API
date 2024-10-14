from .customer_routes import register_customer_routes
from .product_routes import register_product_routes
from .order_routes import register_order_routes

def register_all_routes(app):
    # Register routes with the app
    register_customer_routes(app)
    register_product_routes(app)
    register_order_routes(app)

# Additional route registrations can be added here as needed
