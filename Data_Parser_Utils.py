from bs4 import BeautifulSoup
import aiofiles as aiofiles
import asyncio
import aiohttp


# FILE OPERATIONS
def read_file(path):
    with open(path, "r") as file:
        return file.read()


async def write_to_file(path, content):
    try:
        async with aiofiles.open(path, "a") as file:
            existing_content = read_file(path)
            if content not in existing_content or "SCRIPT" in content:
                await file.write(content + "\n")
    except Exception as e:
        print(f"Error writing to file {path}: {e}")


# OTHER
def discount(old, new):
    x = (old - new) / old * 100
    return round(x, 2)


async def fetch_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            return BeautifulSoup(content, "html.parser")


async def sleep_for_10_minutes():
    await asyncio.sleep(600)
