"""
Creating a program to log into the my disney experience site and check for fastpass tickets

Following a guide located at: https://kazuar.github.io/scraping-tutorial/
"""
import requests
from lxml import html

USERNAME = input("Enter user: ")
PASSWORD = input("Enter password: ")

LOGIN_URL = "https://disneyworld.disney.go.com/login/"
URL = "https://disneyworld.disney.go.com/fastpass-plus/"


def main():
    """
    
    :return: 
    """
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='pep_csrf']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME,
        "password": PASSWORD,
        "pep_csrf": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers=dict(referer=URL))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    print(bucket_names)

if __name__ == '__main__':
    main()
