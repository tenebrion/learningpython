"""
Testing selenium
"""
from selenium import webdriver

# basic values for the selenium driver and website
chrome_driver = r"C:\Users\michael.f.koegel\Documents\Python\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver)
# browser.get("http://inventwithpython.com")
browser.get("https://mail.yahoo.com")

"""
# This section is looking for tags on the site for practice
try:
    elem = browser.find_element_by_class_name("bookcover")
    print("Found <{}> element with that class name!".format(elem.tag_name))
except:
    print("Was not able to find an element with that name.")
"""

"""
# example of how to click a link on a page automatically
link_element = browser.find_element_by_link_text("Read It Online")
link_element.click()  # follows the "Read It Online" link
"""

# setting up some yahoo test log on
email_element = browser.find_element_by_id("login-username")
# since it has to be a real email address, I found something that works
email_element.send_keys("not_real@yahoo.com")
# once the user is entered, we need to click on the login button
click_user_link = browser.find_element_by_id("login-signin")
click_user_link.click()
password_element = browser.find_element_by_id("login-passwd")
# no, this is not the password for the account.
password_element.send_keys("12345")
# once the password is entered, we need to click on the 2nd login button
click_password_link = browser.find_element_by_id("login-signin")
click_password_link.click()
