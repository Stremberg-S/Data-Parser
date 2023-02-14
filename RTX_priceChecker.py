import requests
from bs4 import BeautifulSoup
import time


def write_to_file(content):
    with open("/Users/stremberg_s/Desktop/RTX_4080.txt", "a") as file:
        file.write(content + "\n")


def get_price(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find("span", itemprop="price").get_text(strip=True)
    price = price[:-1].replace("\xa0", "").replace(",", ".")
    return float(price)


def get_item(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    item = soup.find("h1", class_="text-normal fs-3 my-0").get_text(strip=True)
    return item


def main(wanted_price, url):
    price = get_price(url)
    item = get_item(url)
    if price < wanted_price:
        write_to_file(item + "\t" + str(price) + " €")
        time.sleep(600)
    else:
        time.sleep(600)


if __name__ == "__main__":
    write_to_file("\tSCRIPT STARTED.. :)")
    while True:
        try:
            main(1699,
                 "https://www.jimms.fi/fi/Product/Show/186256/rog-strix-rtx4080-o16g-gaming/asus-geforce-rtx-4080-rog"
                 "-strix-oc-edition-naytonohjain-16gb-gddr6x")
            main(1599,
                 "https://www.jimms.fi/fi/Product/Show/187950/gv-n4080aorus-m-16gd/gigabyte-geforce-rtx-4080-aorus-master"
                 "-naytonohjain-16gb-gddr6x")
        except:
            write_to_file("\tSCRIPT STOPPED.. :(")
            break
