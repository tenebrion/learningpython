#! python3
"""
lucky.py - Opens several Google search results
"""
import requests
import sys
import webbrowser
import bs4

print("Googling.......")  # display text while downloading the Google page
res = requests.get("https://www.google.com/search?q={}".format(" ".join(sys.argv[1:])))
res.raise_for_status()

# Retrieve top search results
soup = bs4.BeautifulSoup(res.text, "lxml")

# Open a browser tab for each result
link_elements = soup.select(".r a")
number_open = min(5, len(link_elements))
for i in range(number_open):
    webbrowser.open("https://www.google.com" + link_elements[i].get("href"))
