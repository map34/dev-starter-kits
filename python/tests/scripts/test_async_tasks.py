from unittest import IsolatedAsyncioTestCase, mock
from package.scripts.async_tasks import sum

class Test(IsolatedAsyncioTestCase):

    @mock.patch("asyncio.sleep")
    async def test_sum(self, *_):
        result = await sum("A", [1, 2, 3])
        self.assertEqual(result, 6)
