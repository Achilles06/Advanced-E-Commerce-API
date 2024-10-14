import unittest
from unittest.mock import patch
from app import app

class ProductTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('services.product_service.db')
    def test_create_product(self, mock_db):
        response = self.app.post('/api/products', json={
            "name": "Laptop",
            "price": 1200.99
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("Product created successfully", response.json['message'])

    def test_get_product(self):
        response = self.app.get('/api/products/1')
        if response.status_code == 200:
            self.assertIn("name", response.json)
            self.assertIn("price", response.json)
        else:
            self.assertEqual(response.status_code, 404)

    @patch('services.product_service.db')
    def test_update_product(self, mock_db):
        response = self.app.put('/api/products/1', json={
            "name": "Smartphone",
            "price": 799.99
        })
        self.assertIn(response.status_code, [200, 404])

    def test_delete_product(self):
        response = self.app.delete('/api/products/1')
        self.assertIn(response.status_code, [200, 404])

    def test_list_products(self):
        response = self.app.get('/api/products')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
