from configparser import ParsingError
from bs4 import BeautifulSoup
import aiofiles as aiofiles
import aiohttp


async def write_to_file(content):
    async with aiofiles.open("/Users/stremberg_s/Desktop/RTX_4080.txt", "a") as file:
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


def discount(old, new):
    x = (old - new) / old * 100
    return round(x, 2)


async def main(wanted_price, url):
    try:
        price = await get_price(url)
        item = await get_item(url)
        if price < wanted_price:
            x = discount(wanted_price, price)
            await write_to_file(item + "\t" +
                                str(price) + " €" + "\t-" +
                                str(x) + "%")
    except ParsingError:
        pass
