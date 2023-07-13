from Data_Parser_Utils import *
from Path import *


async def get_price(store, url):
    """Retrieve the price of a product from a given store and URL.

    Args:
        store (str): The name of the store.
        url (str): The URL of the product page.
    Returns:
        float: The price of the product.
    """
    path = ALL_STORES
    price = 0
    try:
        soup = await fetch_html(url)

        if store == "Jimms":
            path = JIMMS
            price = soup.find("span", itemprop="price").get_text(strip=True)
        elif store == "Marimekko":
            path = MARIMEKKO
            price = soup.find(
                "div",
                class_="pdp-title-row__price product-info-price typo--heading-small "
                       "typo--heading-medium---l-up",
            ).get_text(strip=True)
        price = price[:-1].replace("\xa0", "").replace(",", ".")

        return float(price)

    except (AttributeError, ValueError):
        return await write_to_file(path, "\tCan't find the price")
    except Exception as e:
        return await write_to_file(path, f"\tError getting price: {e}")


async def get_item(store, url):
    """
    Retrieves the available status of an item from the
        specified store's webpage.

    Args:
        store (str): The name of the store.
        url (str): The URL of the item.
    Returns:
        str: The available status of the item.
    """
    path = ALL_STORES
    item = ""
    try:
        soup = await fetch_html(url)

        if store == "Jimms":
            path = JIMMS
            item = soup.find(
                "h1", class_="text-normal fs-3 my-0"
            ).get_text(strip=True)
        elif store == "Marimekko":
            path = MARIMEKKO
            item = soup.find(
                "a", href=url
            ).get_text(strip=True)

        return item

    except (AttributeError, TypeError):
        return await write_to_file(path, "\tCan't find the item")
    except Exception as e:
        return await write_to_file(path, f"\tError getting item: {e}")


async def get_available_status(store, url):
    """
    Retrieves the available status of an item from the
        specified store's webpage.

    Args:
        store (str): The name of the store.
        url (str): The URL of the item.
    Returns:
        str: The available status of the item.
    """
    path = ALL_STORES
    status = ""
    try:
        soup = await fetch_html(url)

        if store == "Jimms":
            path = JIMMS
            status_element = soup.find(
                "span", class_="availability-text d-flex align-items-center gap-1"
            )
            if status_element is not None:
                status = status_element.get_text(strip=True).replace(
                    "fiber_manual_record", ""
                )
        elif store == "Marimekko":
            path = MARIMEKKO
            status_element = soup.find(
                "ul", {"class": "pdp__delivery-list typo--body-small"}
            ).find_all("li")[1]
            if status_element is not None:
                status = status_element.get_text(strip=True)

        return status

    except (AttributeError, TypeError):
        return await write_to_file(path, "\tCan't find the status")
    except Exception as e:
        return await write_to_file(path, f"\tError getting status: {e}")


async def parse_data(store, wanted_price, url):
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
    path = ALL_STORES
    try:
        if store == "Jimms":
            path = JIMMS
        elif store == "Marimekko":
            path = MARIMEKKO

        price = await get_price(store, url)
        item = await get_item(store, url)
        status = await get_available_status(store, url)

        if price < wanted_price:
            x = discount(wanted_price, price)
            await write_to_file(
                path,
                str(item)
                + "\t | "
                + str(price)
                + " €"
                + " | -"
                + str(x)
                + " %"
                + " | "
                + str(status),
            )
    except (AttributeError, TypeError):
        pass
    except Exception as e:
        return await write_to_file(path, f"\tError parsing data: {e}")
