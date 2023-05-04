import requests
from bs4 import BeautifulSoup


def get_prices(url):
    doc = requests.get(url)
    doc = BeautifulSoup(doc.text, "html.parser")
    rubles = doc.find_all(string="₽")

    list_of_prices = list()

    for r in rubles:
        str = r.parent.parent.text.strip()
        if len(str) > 15:
            str = str[15:].strip()
        num = int(str.replace(" ", "").replace("₽", ""))
        list_of_prices.append(num)

    return list_of_prices


def get_max_price(url):
    doc = requests.get(url)
    doc = BeautifulSoup(doc.text, "html.parser")
    rubles = doc.find_all(string="₽")

    list_of_prices = list()

    max_p_url = ""
    max_p = 0
    for r in rubles:
        str = r.parent.parent.text.strip()
        if len(str) > 15:
            str = str[15:].strip()
        num = int(str.replace(" ", "").replace("₽", ""))

        if max_p < num:
            max_p_url = r.parent.parent.parent.parent.parent.find("a")["href"]
        max_p = max(max_p, num)

    return max_p, max_p_url
