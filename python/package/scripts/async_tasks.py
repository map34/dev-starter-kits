import asyncio
import requests

async def sleep():
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    return total

async def get(url):
    result = requests.get(url)
    print(f"GET {url} finished")
    return result


async def execute_tasks():
    return await asyncio.gather(
        sum("A", [1, 2, 3, 4, 5]),
        get("https://google.com")
    )

def main():
    loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(execute_tasks())
        print(result)
    finally:
        loop.close()

if __name__ == '__main__':
    main()
