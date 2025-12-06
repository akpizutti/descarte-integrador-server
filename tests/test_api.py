from app import create_app
import json
import unittest

class TestWasteCollectionAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()

    def test_version_endpoint(self):
        response = self.client.get('/api/v1/version')
        self.assertEqual(response.status_code, 200)
        self.assertIn('version', json.loads(response.data))

    def test_locations_endpoint(self):
        response = self.client.get('/api/v1/locations')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

if __name__ == '__main__':
    unittest.main()