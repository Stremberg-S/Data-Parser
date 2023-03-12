from configparser import ParsingError
from Data_Parser_Utils import *


async def get_price(store, url):
    price = 0
    try:
        soup = await fetch_html(url)

        if store == "Jimms":
            price = soup.find("span", itemprop="price").get_text(strip=True)
        elif store == "Marimekko":
            price = soup.find("div", class_="pdp-title-row__price product-info-price typo--heading-small "
                                            "typo--heading-medium---l-up").get_text(strip=True)
        price = price[:-1].replace("\xa0", "").replace(",", ".")

        return float(price)
    except (ParsingError, AttributeError):
        return await write_to_file("\tCan't find the price")


async def get_item(store, url):
    item = ""
    try:
        soup = await fetch_html(url)

        if store == "Jimms":
            item = soup.find("h1", class_="text-normal fs-3 my-0").get_text(strip=True)
        elif store == "Marimekko":
            item = soup.find("a", href=url).get_text(strip=True)

        return item
    except (ParsingError, AttributeError):
        return await write_to_file("\tCan't find the item")


async def get_available_status(store, url):
    status = ""
    try:
        soup = await fetch_html(url)

        if store == "Jimms":
            status_element = soup.find("span", class_="availability-text d-flex align-items-center gap-1")
            if status_element is not None:
                status = status_element.get_text(strip=True).replace("fiber_manual_record", "")
        elif store == "Marimekko":
            status_element = soup.find("ul", {"class": "pdp__delivery-list typo--body-small"}).find_all('li')[1]
            if status_element is not None:
                status = status_element.get_text(strip=True)

    except (ParsingError, AttributeError):
        return await write_to_file("\tCan't find the status")
    return status


async def parse_data(store, wanted_price, url):
    try:
        price = await get_price(store, url)
        item = await get_item(store, url)
        status = await get_available_status(store, url)

        if price < wanted_price:
            x = discount(wanted_price, price)
            await write_to_file(str(item) + "\t | " +
                                str(price) + " €" +
                                " | -" + str(x) + " %" +
                                " | " + str(status))
    except (ParsingError, AttributeError):
        pass
