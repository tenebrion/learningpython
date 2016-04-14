"""
Creating a program to connect to Wikipedia and display content.
"""
import json
from urllib.request import urlopen
import webbrowser




class Wikipedia:
    """
    Testing this out
    """
    page = "https://en.wikipedia.org/wiki?curid="
    url = "https://en.wikipedia.org//w/api.php?action=query&format=json&list=random"

    def __init__(self, page):
        self.page = page

    def random_page(self):
        """
        simple method to randomly fetch new pages
        :return:
        """
        response = urlopen(self.url).read().decode('utf8')
        obj = json.loads(response)
        description = obj["query"]["random"][0]["title"]
        pageid = obj["query"]["random"][0]["id"]

print("Welcome to my random Wikipedia page generator.\n"
      "A page title will appear. If you would like to read the page, press y for yes.\n"
      "Otherwise, select n for no, which will pull a different page.\n"
      "When you are done, press enter to quit.")

