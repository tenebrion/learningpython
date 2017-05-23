"""
Web scraping on automate the boring stuff - ch. 11
"""
import requests
import bs4

res = requests.get("http://nostarch.com")
res.raise_for_status()
no_starch = bs4.BeautifulSoup(res.text, "lxml")
print(type(no_starch))