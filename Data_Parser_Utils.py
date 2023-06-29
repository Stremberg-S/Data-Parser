import asyncio

import aiofiles as aiofiles
import aiohttp
from bs4 import BeautifulSoup


# FILE OPERATIONS
def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


async def write_to_file(path, content):
    try:
        async with aiofiles.open(path, "a") as file:
            existing_content = read_file(path)
            if content not in existing_content:
                await file.write(content + "\n")
    except Exception as e:
        print(f"Error writing to file {path}: {e}")


# OTHER
def discount(old, new):
    """
    Calculates the percentage change between an old value and a new value.

    Args:
        old (float): The old value.
        new (float): The new value.
    Returns:
        float: The percentage change rounded to 2 decimal places.
    """
    x = (old - new) / old * 100
    return round(x, 2)


async def fetch_html(url):
    """
    Fetches the HTML content of a webpage using an asynchronous HTTP client session.

    Args:
        url (str): The URL of the webpage.
    Returns:
        BeautifulSoup: The BeautifulSoup object representing the parsed HTML content.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            return BeautifulSoup(content, "html.parser")


async def sleep_for_10_minutes():
    await asyncio.sleep(600)
