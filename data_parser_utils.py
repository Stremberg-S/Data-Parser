import asyncio

import aiofiles
import aiohttp
from bs4 import BeautifulSoup


# FILE OPERATIONS
def read_file(path: str) -> str:
    """Read the contents of a file and return them as a string.

    Args:
        path (str): The path to the file.
    Returns:
        str: The contents of the file.

    """
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


async def write_to_file(path: str, content: str):
    """Append content to a file asynchronously.

    Args:
        path (str): The path to the file.
        content (str): The content to be appended.

    Raises:
        OSError: If there is an error opening or writing to the file.

    """
    try:
        async with aiofiles.open(path, "a") as file:
            existing_content = read_file(path)
            if content not in existing_content:
                await file.write(content + "\n")
    except Exception as error:
        print(f"Error writing to file {path}: {error}")


# OTHER
def discount(old: float, new: float) -> float:
    """
    Calculates the percentage change between an old value and a new value.

    Args:
        old (float): The old value.
        new (float): The new value.
    Returns:
        float: The percentage change rounded to 2 decimal places.

    """
    percentage_change = (old - new) / old * 100
    return round(percentage_change, 2)


async def fetch_html(url):
    """
    Fetches the HTML content of a webpage using an asynchronous
        HTTP client session.

    Args:
        url (str): The URL of the webpage.
    Returns:
        BeautifulSoup: The BeautifulSoup object representing the parsed
            HTML content.

    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            return BeautifulSoup(content, "html.parser")


async def sleep_for_10_minutes():
    """
    Asynchronous function suspends the execution for 10 minutes.

    This function uses asyncio.sleep to pause the execution of the current
        coroutine for the specified duration of 10 minutes (600 seconds).

    """
    await asyncio.sleep(600)
