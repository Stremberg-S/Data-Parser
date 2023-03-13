from Data_Parser_Utils import *
from Path import *


async def get_price(store, url):
    path = all_stores
    price = 0
    try:
        soup = await fetch_html(url)

        if store == "Jimms":
            path = jimms
            price = soup.find("span", itemprop="price").get_text(strip=True)
        elif store == "Marimekko":
            path = marimekko
            price = soup.find("div", class_="pdp-title-row__price product-info-price typo--heading-small "
                                            "typo--heading-medium---l-up").get_text(strip=True)
        price = price[:-1].replace("\xa0", "").replace(",", ".")

        return float(price)
    except (AttributeError, ValueError):
        return await write_to_file(path, "\tCan't find the price")
    except Exception as e:
        return await write_to_file(path, "\tError getting price: {}".format(e))


async def get_item(store, url):
    path = all_stores
    item = ""
    try:
        soup = await fetch_html(url)

        if store == "Jimms":
            path = jimms
            item = soup.find("h1", class_="text-normal fs-3 my-0").get_text(strip=True)
        elif store == "Marimekko":
            path = marimekko
            item = soup.find("a", href=url).get_text(strip=True)

        return item
    except (AttributeError, TypeError):
        return await write_to_file(path, "\tCan't find the item")
    except Exception as e:
        return await write_to_file(path, "\tError getting item: {}".format(e))


async def get_available_status(store, url):
    path = all_stores
    status = ""
    try:
        soup = await fetch_html(url)

        if store == "Jimms":
            path = jimms
            status_element = soup.find("span", class_="availability-text d-flex align-items-center gap-1")
            if status_element is not None:
                status = status_element.get_text(strip=True).replace("fiber_manual_record", "")
        elif store == "Marimekko":
            path = marimekko
            status_element = soup.find("ul", {"class": "pdp__delivery-list typo--body-small"}).find_all('li')[1]
            if status_element is not None:
                status = status_element.get_text(strip=True)

        return status
    except (AttributeError, TypeError):
        return await write_to_file(path, "\tCan't find the status")
    except Exception as e:
        return await write_to_file(path, "\tError getting status: {}".format(e))


async def parse_data(store, wanted_price, url):
    path = all_stores
    try:
        if store == "Jimms":
            path = jimms
        elif store == "Marimekko":
            path = marimekko

        price = await get_price(store, url)
        item = await get_item(store, url)
        status = await get_available_status(store, url)

        if price < wanted_price:
            x = discount(wanted_price, price)
            await write_to_file(path,
                                str(item) + "\t | " +
                                str(price) + " €" +
                                " | -" + str(x) + " %" +
                                " | " + str(status))
    except (AttributeError, TypeError):
        pass
    except Exception as e:
        return await write_to_file(path, "\tError parsing data: {}".format(e))
