from package import compute
import unittest

class MainTests(unittest.TestCase):

    def setUp(self):
        super().setUp()

    def test_main(self):
        compute.return_random()

    def tearDown(self):
        super().tearDown()


if __name__ == '__main__':
    unittest.main()
