from package import execute
import unittest
from unittest import mock


def mocked_requests_get(*args, **kwargs):
    class MockResponse():
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            self.headers = json_data

        def json(self):
            return self.json_data

    if args[0] == 'https://google.com':
        return MockResponse({"key1": "value1"}, 200)

    return MockResponse(None, 404)


class ExecuteTests(unittest.TestCase):

    def setUp(self):
        super().setUp()

    @mock.patch("requests.get", side_effect=mocked_requests_get)
    @mock.patch("package.scripts.async_tasks.main")
    def test_main(self, *args):
        value = execute.main()
        assert isinstance(value, dict)

    def tearDown(self):
        super().tearDown()


if __name__ == '__main__':
    unittest.main()
