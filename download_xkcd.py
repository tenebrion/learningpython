#! python3
"""
download_xkcd.py - Downloads every single XKCD comic
"""
import requests
import os
import bs4

url = "http://xkcd.com"  # starting url
os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd
while not url.endswith("#"):
    # download the page
    print("Downloading page {}...".format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "lxml")

    # find the url of the comic image
    comic_element = soup.select("#comic img")
    if comic_element is []:
        print("Could not find comic image!")
    else:
        try:
            comic_url = "http:" + comic_element[0].get("src")
            # download the image
            print("Downloading image {}...".format(comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            previous_link = soup.select('a[rel="prev"]')[0]
            url = "http://xkcd.com{}".format(previous_link.get("href"))
            continue

        # Save the image to ./xkcd
        image_file = open(os.path.join("xkcd", os.path.basename(comic_url)), "wb")
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    # Get the Previous button's url
    previous_link = soup.select('a[rel="prev"]')[0]
    url = "http://xkcd.com{}".format(previous_link.get("href"))

print("Done.")
