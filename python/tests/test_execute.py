from package import execute
import unittest


class ExecuteTests(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        pass

    def test_main(self):
        execute.main()

    def tearDown(self) -> None:
        super().tearDown()
        pass


if __name__ == '__main__':
    unittest.main()
