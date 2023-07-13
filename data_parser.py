from data_parser_utils import (discount, fetch_html, get_correct_path,
                               write_to_file)
from path import JIMMS, MARIMEKKO


async def get_price(store: str, url: str) -> float:
    """Retrieve the price of a product from a given store and URL.

    Args:
        store (str): The name of the store.
        url (str): The URL of the product page.
    Returns:
        float: The price of the product.

    """
    path: str = get_correct_path(store)
    price: str = '0'
    
    try:
        soup = await fetch_html(url)

        if path == JIMMS:
            price = soup.find("span", itemprop="price").get_text(strip=True)

        elif path == MARIMEKKO:
            price = soup.find(
                "div",
                class_="pdp-title-row__price product-info-price typo--heading-small "
                       "typo--heading-medium---l-up",
            ).get_text(strip=True)

        price = price[:-1].replace("\xa0", "").replace(",", ".")

        return float(price)

    except (AttributeError, ValueError):
        return await write_to_file(path, "\tCan't find the price")
    except Exception as error:
        return await write_to_file(path, f"\tError getting price: {error}")


async def get_item(store: str, url: str) -> str:
    """
    Retrieves the available status of an item from the
        specified store's webpage.

    Args:
        store (str): The name of the store.
        url (str): The URL of the item.
    Returns:
        str: The available status of the item.

    """
    path: str = get_correct_path(store)
    item: str = ""

    try:
        soup = await fetch_html(url)

        if path == JIMMS:
            item = soup.find(
                "h1", class_="text-normal fs-3 my-0"
            ).get_text(strip=True)

        elif path == MARIMEKKO:
            item = soup.find(
                "a", href=url
            ).get_text(strip=True)

        return item

    except (AttributeError, TypeError):
        return await write_to_file(path, "\tCan't find the item")
    except Exception as error:
        return await write_to_file(path, f"\tError getting item: {error}")


async def get_available_status(store: str, url: str) -> str:
    """
    Retrieves the available status of an item from the
        specified store's webpage.

    Args:
        store (str): The name of the store.
        url (str): The URL of the item.
    Returns:
        str: The available status of the item.

    """
    path: str = get_correct_path(store)
    status: str = "unknown status"

    try:
        soup = await fetch_html(url)

        if path == JIMMS:
            status_element = soup.find(
                "span", class_="availability-text d-flex align-items-center gap-1"
            )
            if status_element is not None:
                status = status_element.get_text(strip=True).replace(
                    "fiber_manual_record", ""
                )

        elif path == MARIMEKKO:
            status_element = soup.find(
                "ul", {"class": "pdp__delivery-list typo--body-small"}
            ).find_all("li")[1]
            if status_element is not None:
                status = status_element.get_text(strip=True)

        return status

    except (AttributeError, TypeError):
        return await write_to_file(path, "\tCan't find the status")
    except Exception as error:
        return await write_to_file(path, f"\tError getting status: {error}")


async def parse_data(store: str, wanted_price: float, url: str) -> None:
    """
    Parses data for a given store, comparing the price of an item with
        the wanted price, and writes the item details to a file if the
        price is lower than the wanted price.

    Args:
        store (str): The name of the store.
        wanted_price (float): The desired price for the item.
        url (str): The URL of the item.
    Returns:
        None

    """
    path: str = get_correct_path(store)

    try:
        price = await get_price(store, url)
        item = await get_item(store, url)
        status = await get_available_status(store, url)

        if price < wanted_price:
            percentage_change = discount(wanted_price, price)
            content = f"{item} | {price} € | -{percentage_change} % | {status}"
            await write_to_file(path, content)

    except (AttributeError, TypeError):
        pass
    except Exception as error:
        return await write_to_file(path, f"\tError parsing data: {error}")
