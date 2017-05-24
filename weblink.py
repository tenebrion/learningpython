"""
Trying to crawl an angular JS site
"""
import selenium
from selenium import webdriver
import time

LOGIN_URL = "https://disneyworld.disney.go.com/login/"
URL = "https://disneyworld.disney.go.com/fastpass-plus/"


def main(url, run_headless=True):
    """
    
    :param url: 
    :param run_headless: 
    :return: 
    """
    if run_headless:
        # display = Display(visible=0, size=(1024,768))
        # display.start()
        pass

    browser = webdriver.Chrome()
    login_url = LOGIN_URL
    browser.get(login_url)
    time.sleep(15)
    element = browser.find_element_by_xpath('/html/body')
    print(element)

if __name__ == '__main__':
    main(URL)
