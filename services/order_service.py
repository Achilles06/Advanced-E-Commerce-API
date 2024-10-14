from models import db
from models.order import Order
from models.customer import Customer
from datetime import datetime
from flask import jsonify

class OrderService:

    @staticmethod
    def create_order(data, customer_id):
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify({"error": "Customer not found"}), 404
        
        # Creating an order instance and setting its properties
        order = Order(order_date=datetime.utcnow(), customer_id=customer_id)
        db.session.add(order)
        db.session.commit()

        # Link products to the order (assumes data contains product and quantity info)
        # Here, you'd add logic to link ordered products to the order

        return jsonify({"message": "Order placed successfully", "id": order.id}), 201

    @staticmethod
    def get_order(id, customer_id):
        order = Order.query.filter_by(id=id, customer_id=customer_id).first()
        if order:
            return jsonify({
                "id": order.id,
                "order_date": order.order_date.isoformat(),
                "customer_id": order.customer_id,
                # Include additional order details, such as products, if implemented
            }), 200
        return jsonify({"error": "Order not found"}), 404
