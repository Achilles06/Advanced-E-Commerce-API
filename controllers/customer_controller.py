from flask import Blueprint, request, jsonify
from services.customer_service import CustomerService
from flask_jwt_extended import jwt_required

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customers', methods=['POST'])
@jwt_required()
def add_customer():
    data = request.json
    return CustomerService.create_customer(data)

@customer_bp.route('/customers/<int:id>', methods=['GET'])
@jwt_required()
def get_customer(id):
    return CustomerService.get_customer(id)

@customer_bp.route('/customers/<int:id>', methods=['PUT'])
@jwt_required()
def update_customer(id):
    data = request.json
    return CustomerService.update_customer(id, data)

@customer_bp.route('/customers/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_customer(id):
    return CustomerService.delete_customer(id)
