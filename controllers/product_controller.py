from flask import Blueprint, request, jsonify
from services.product_service import ProductService
from flask_jwt_extended import jwt_required

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['POST'])
@jwt_required()
def add_product():
    """Create a new product"""
    data = request.json
    return ProductService.create_product(data)

@product_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    """Retrieve a product by ID"""
    return ProductService.get_product(id)

@product_bp.route('/products/<int:id>', methods=['PUT'])
@jwt_required()
def update_product(id):
    """Update product details by ID"""
    data = request.json
    return ProductService.update_product(id, data)

@product_bp.route('/products/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_product(id):
    """Delete a product by ID"""
    return ProductService.delete_product(id)

@product_bp.route('/products', methods=['GET'])
def list_products():
    """List all products"""
    return ProductService.list_products()
