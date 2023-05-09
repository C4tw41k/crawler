import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35"
}

content = requests.get("https://www.chanel.cn/cn/fragrance/women/c/7x1x1x30/n5/", headers=headers).text


soup = BeautifulSoup(content, "html.parser")

all_names = soup.find_all("span", attrs={"data-product-element":"description"})

i = 1
for name in all_names:
    print(name.string)
    print(i)
    i = i + 1