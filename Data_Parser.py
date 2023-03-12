from Path import *
from configparser import ParsingError
from bs4 import BeautifulSoup
import aiofiles as aiofiles
import aiohttp


def read_file():
    with open(jimms, "r") as file:
        return file.read()


async def write_to_file(content):
    async with aiofiles.open(jimms, "a") as file:
        existing_content = read_file()
        if content not in existing_content or "SCRIPT" in content:
            await file.write(content + "\n")


async def get_price(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.text()
                soup = BeautifulSoup(content, "html.parser")
                price = soup.find("span", itemprop="price").get_text(strip=True)
                price = price[:-1].replace("\xa0", "").replace(",", ".")
                return float(price)
    except ParsingError:
        return await write_to_file("\tCan't find the price")


async def get_item(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.text()
                soup = BeautifulSoup(content, "html.parser")
                item = soup.find("h1", class_="text-normal fs-3 my-0").get_text(strip=True)
                return item
    except ParsingError:
        return await write_to_file("\tCan't find the item")


async def get_available_status(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.text()
                soup = BeautifulSoup(content, "html.parser")
                status_element = soup.find("span", class_="availability-text d-flex align-items-center gap-1")
                if status_element is not None:
                    status = status_element.get_text(strip=True).replace("fiber_manual_record", "")
                    return status
    except ParsingError:
        return await write_to_file("\tCan't find the status")


def discount(old, new):
    x = (old - new) / old * 100
    return round(x, 2)


async def parse_data(wanted_price, url):
    try:
        price = await get_price(url)
        item = await get_item(url)
        status = await get_available_status(url)

        if price < wanted_price:
            x = discount(wanted_price, price)
            await write_to_file(item + "\t | " +
                                str(price) + " €" +
                                " | -" + str(x) + " %" +
                                " | " + str(status))
    except ParsingError:
        pass
