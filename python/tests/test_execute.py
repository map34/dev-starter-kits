from package import main
import unittest

class ExecuteTests(unittest.TestCase):

    def setUp(self):
        super().setUp()

    def test_main(self):
        main.main()

    def tearDown(self):
        super().tearDown()


if __name__ == '__main__':
    unittest.main()
