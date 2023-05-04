import requests


url = "https://domclick.ru/arenda/kvartiry"

doc = requests.get(url)

print(doc.text)