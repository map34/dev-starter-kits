import unittest
import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_hello(self):
        res = self.app.get('/hello')
        self.assertEqual(res.status_code, 200)
        self.assertTrue("Hello, World!" in str(res.data))
