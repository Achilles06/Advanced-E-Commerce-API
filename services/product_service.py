from models import db
from models.product import Product
from flask import jsonify

class ProductService:

    @staticmethod
    def create_product(data):
        product = Product(name=data['name'], price=data['price'])
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product created successfully", "id": product.id}), 201

    @staticmethod
    def get_product(id):
        product = Product.query.get(id)
        if product:
            return jsonify({"id": product.id, "name": product.name, "price": product.price}), 200
        return jsonify({"error": "Product not found"}), 404

    @staticmethod
    def update_product(id, data):
        product = Product.query.get(id)
        if product:
            product.name = data.get('name', product.name)
            product.price = data.get('price', product.price)
            db.session.commit()
            return jsonify({"message": "Product updated successfully"}), 200
        return jsonify({"error": "Product not found"}), 404

    @staticmethod
    def delete_product(id):
        product = Product.query.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return jsonify({"message": "Product deleted successfully"}), 200
        return jsonify({"error": "Product not found"}), 404

    @staticmethod
    def list_products():
        products = Product.query.all()
        product_list = [{"id": product.id, "name": product.name, "price": product.price} for product in products]
        return jsonify(product_list), 200
