from package.scripts import async_tasks
from sortedcontainers import SortedDict
import requests


def main():
    async_tasks.main()
    result = requests.get("https://google.com")
    sorted_result = SortedDict(result.headers)
    return sorted_result

if __name__ == '__main__':
    main()
