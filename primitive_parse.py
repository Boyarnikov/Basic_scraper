import requests
from selenium import webdriver

url = "https://move.ru/arenda_kvartir/v_predelah_mkad/?limit=30"

doc = requests.get(url)


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches


t = doc.text
all_indexes = find_all(t, "&#8381")
for i in all_indexes:
    print(t[i-26:i+20])
