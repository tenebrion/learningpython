"""
Creating a program to connect to Wikipedia and display content.
"""
import json
from urllib.request import urlopen
import webbrowser

# here is the page url format and the url of the 'random' page.
page = "https://en.wikipedia.org/wiki?curid="
url = "https://en.wikipedia.org//w/api.php?action=query&format=json&list=random"


def random_page():
    """
    simple method to randomly fetch new pages
    :return
    """
    response = urlopen(url).read().decode('utf8')
    obj = json.loads(response)
    return obj


def open_page(some_url):
    """
    just a simple method to open a web browser link
    :param some_url: passing te full url to a wikipedia page
    """
    webbrowser.open(some_url)


get_page = random_page()
description = get_page["query"]["random"][0]["title"]
print("The title of the page is {}".format(description))
page_id = get_page["query"]["random"][0]["id"]
open_page(page + str(page_id))
