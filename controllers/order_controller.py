from flask import Blueprint, request, jsonify
from services.order_service import OrderService
from flask_jwt_extended import jwt_required, get_jwt_identity

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders', methods=['POST'])
@jwt_required()
def place_order():
    """Place a new order"""
    current_user = get_jwt_identity()
    data = request.json
    return OrderService.create_order(data, current_user)

@order_bp.route('/orders/<int:id>', methods=['GET'])
@jwt_required()
def get_order(id):
    """Retrieve an order by ID"""
    current_user = get_jwt_identity()
    return OrderService.get_order(id, current_user)
