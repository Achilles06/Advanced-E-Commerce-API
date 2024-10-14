import unittest
from unittest.mock import patch
from app import app

class OrderTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('services.order_service.db')
    def test_place_order(self, mock_db):
        response = self.app.post('/api/orders', json={
            "customer_id": 1,
            "products": [
                {"product_id": 1, "quantity": 2},
                {"product_id": 2, "quantity": 1}
            ]
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("Order placed successfully", response.json['message'])

    def test_get_order(self):
        response = self.app.get('/api/orders/1')
        if response.status_code == 200:
            self.assertIn("order_date", response.json)
            self.assertIn("customer_id", response.json)
        else:
            self.assertEqual(response.status_code, 404)
