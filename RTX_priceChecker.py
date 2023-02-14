import requests
from bs4 import BeautifulSoup
import time


def get_price():
    page = requests.get(
        "https://www.jimms.fi/fi/Product/Show/186256/rog-strix-rtx4080-o16g-gaming/asus-geforce-rtx-4080-rog-strix-oc-edition-naytonohjain-16gb-gddr6x")
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find("span", class_="pricetext").get_text(strip=True)
    price = price[:-1].replace("\xa0", "").replace(",", ".")
    return float(price)


def main():
    target_price = 1699

    while True:
        price = get_price()
        name = "Asus GeForce RTX 4080 ROG Strix - OC Edition"

        if price <= target_price:
            with open("/Users/stremberg_s/Desktop/RTX 4080.txt", "a") as file:
                file.write("\n" + name + "\t" + str(price))
            time.sleep(1800)
        else:
            time.sleep(1800)


if __name__ == "__main__":
    main()
