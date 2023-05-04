import requests
from selenium import webdriver

url = "https://domclick.ru/arenda/kvartiry"

doc = requests.get(url)

print("+++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++")
print("Страничка полученная через request")
print(doc.text)

driver = webdriver.Chrome()
driver.get(url)

print("+++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++")
print("Страничка полученная через Chrome")
print(driver.page_source)
