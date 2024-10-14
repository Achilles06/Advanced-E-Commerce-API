from models import db
from models.customer import Customer
from flask import jsonify

class CustomerService:

    @staticmethod
    def create_customer(data):
        customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
        db.session.add(customer)
        db.session.commit()
        return jsonify({"message": "Customer created successfully", "id": customer.id}), 201

    @staticmethod
    def get_customer(id):
        customer = Customer.query.get(id)
        if customer:
            return jsonify({"id": customer.id, "name": customer.name, "email": customer.email, "phone": customer.phone}), 200
        return jsonify({"error": "Customer not found"}), 404

    @staticmethod
    def update_customer(id, data):
        customer = Customer.query.get(id)
        if customer:
            customer.name = data.get('name', customer.name)
            customer.email = data.get('email', customer.email)
            customer.phone = data.get('phone', customer.phone)
            db.session.commit()
            return jsonify({"message": "Customer updated successfully"}), 200
        return jsonify({"error": "Customer not found"}), 404

    @staticmethod
    def delete_customer(id):
        customer = Customer.query.get(id)
        if customer:
            db.session.delete(customer)
            db.session.commit()
            return jsonify({"message": "Customer deleted successfully"}), 200
        return jsonify({"error": "Customer not found"}), 404
