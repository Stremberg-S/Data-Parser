import aiofiles as aiofiles
import aiohttp
from bs4 import BeautifulSoup

from Path import *


# FILE OPERATIONS
def read_file():
    with open(all_stores, "r") as file:
        return file.read()


async def write_to_file(content):
    async with aiofiles.open(all_stores, "a") as file:
        existing_content = read_file()
        if content not in existing_content or "SCRIPT" in content:
            await file.write(content + "\n")


# OTHER
def discount(old, new):
    x = (old - new) / old * 100
    return round(x, 2)


async def fetch_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            return BeautifulSoup(content, "html.parser")
