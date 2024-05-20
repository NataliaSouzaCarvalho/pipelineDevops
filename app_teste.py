import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
  def setUp(self):
    self.client = app.test_client()
  def test_devops(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Germinare', response.data)
if _name_ == '_main_':
  unittest.main()
