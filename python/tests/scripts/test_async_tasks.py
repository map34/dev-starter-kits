from unittest import IsolatedAsyncioTestCase, mock
from package.scripts.async_tasks import sum
from package.scripts.async_tasks import get

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

class AsyncTasksTest(IsolatedAsyncioTestCase):

    @mock.patch("asyncio.sleep")
    async def test_sum(self, *_):
        result = await sum("A", [1, 2, 3])
        self.assertEqual(result, 6)

    @mock.patch("requests.get", mocked_requests_get)
    async def test_get(self, *_):
        result = await get("https://google.com")
        self.assertEqual(result.status_code, 200)
