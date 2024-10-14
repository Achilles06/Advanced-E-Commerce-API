import unittest
from unittest.mock import patch
from app import app

class CustomerAccountTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('services.customer_service.db')
    def test_create_customer_account(self, mock_db):
        response = self.app.post('/api/customers/1/account', json={
            "username": "john_doe",
            "password": "secure_password"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("Customer account created successfully", response.json['message'])

    def test_get_customer_account(self):
        response = self.app.get('/api/customers/1/account')
        if response.status_code == 200:
            self.assertIn("username", response.json)
        else:
            self.assertEqual(response.status_code, 404)

    @patch('services.customer_service.db')
    def test_update_customer_account(self, mock_db):
        response = self.app.put('/api/customers/1/account', json={
            "username": "jane_doe",
            "password": "new_secure_password"
        })
        self.assertIn(response.status_code, [200, 404])

    def test_delete_customer_account(self):
        response = self.app.delete('/api/customers/1/account')
        self.assertIn(response.status_code, [200, 404])
