"""
Creating a program to connect to Wikipedia and display content.
"""
import json
from urllib.request import urlopen

url = "https://en.wikipedia.org//w/api.php?action=query&format=json&list=random"
response = urlopen(url).read().decode('utf8')
obj = json.loads(response)
print(obj)