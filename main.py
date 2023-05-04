import requests
from get_prices_from_page import get_prices, get_max_price
from selenium import webdriver
from bs4 import BeautifulSoup
import re

page = 1

url = f"https://move.ru/arenda_kvartir/v_predelah_mkad/?page=1&limit=30"
doc = requests.get(url)
doc = BeautifulSoup(doc.text, "html.parser")


pages_numbers = doc.find_all(class_="pagination-block__page-link")
numbers = [-1 if p.text.strip() == "..." else int(p.text.strip()) for p in pages_numbers]
print(numbers)

pages = numbers[-1]

list_of_prices = list()
max_price = 0
link = ""

for i in range(1, pages):
    url = f"https://move.ru/arenda_kvartir/v_predelah_mkad/?page={i}&limit=30"
    print(f"Смотрим на {i}-тую страницу")
    m, l = get_max_price(url)
    if max_price < m:
        link = l
    max_price = max(m, max_price)
    print(max_price, link)



