import requests
from bs4 import BeautifulSoup
from configparser import ParsingError


def write_to_file(content):
    with open("/Users/stremberg_s/Desktop/RTX_4080.txt", "a") as file:
        file.write(content + "\n")


def get_price(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        price = soup.find("span", itemprop="price").get_text(strip=True)
        price = price[:-1].replace("\xa0", "").replace(",", ".")
        return float(price)
    except ParsingError:
        return write_to_file("\tCan't find the price")


def get_item(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        item = soup.find("h1", class_="text-normal fs-3 my-0").get_text(strip=True)
        return item
    except ParsingError:
        return write_to_file("\tCan't find the item")


def main(wanted_price, url):
    try:
        price = get_price(url)
        item = get_item(url)
        print(item + "\t" + str(price))
        if price < wanted_price:
            write_to_file(item + "\t" + str(price) + " €")
    except ParsingError:
        pass
