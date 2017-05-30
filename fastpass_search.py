"""
Creating a program to log into the my disney experience site and check for fastpass tickets

Future version: Check for fastpass tickets. If there are tickets I want, try to add them to
my account. If there are issues, send a text message to me so I can login on my phone
and add them to my account.
"""
from selenium import webdriver
import time

# Setting up User / Password so that it loads prior to the browser opening
USERNAME = input("Enter user: ")
PASSWORD = input("Enter password: ")

# Loading Chrome and setting basic info.
chrome_driver = r"C:\Users\michael.f.koegel\Documents\Python\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver)
browser.get("https://disneyworld.disney.go.com/login/")

# setting up the log on process (User / Pass)
email_element = browser.find_element_by_id("loginPageUsername")
email_element.send_keys(USERNAME)
password_element = browser.find_element_by_id("loginPagePassword")
password_element.send_keys(PASSWORD)

# once the password is entered, we need to click on the Sign In button
click_password_link = browser.find_element_by_id("loginPageSubmitButton")
click_password_link.click()

# switching to the FastPass screen
browser.get("https://disneyworld.disney.go.com/fastpass-plus/select-party/")

time.sleep(10)  # need to take a quick nap
add_guests = browser.find_element_by_xpath("//span[.='Select All']")
add_guests.click()

click_next_fastpass = browser.find_element_by_xpath("//div[@class='button next primary']")
click_next_fastpass.click()

time.sleep(5)
next_month = browser.find_element_by_xpath("//div[@class='icon.next']/span")
next_month.click()

next_month = browser.find_element_by_xpath("//span[.='29']")
next_month.click()
