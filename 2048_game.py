#! python3
"""
2048_game.py - Using selenium to play a web based 2048 game
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# basic values for the selenium driver and website
chrome_driver = r"C:\Users\michael.f.koegel\Documents\Python\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver)
browser.get("https://gabrielecirulli.github.io/2048/")
html_element = browser.find_element_by_tag_name("body")
# This will determine if the game has ended
retry_button = browser.find_element_by_class_name("retry-button")

# looping through using a straight forward process. So far, the high score is 5604
while retry_button.is_displayed() == False:
    html_element.send_keys(Keys.ARROW_UP)
    html_element.send_keys(Keys.ARROW_RIGHT)
    html_element.send_keys(Keys.ARROW_DOWN)
    html_element.send_keys(Keys.ARROW_LEFT)

print("Final score: {}".format(browser.find_element_by_class_name("score-container").text))
