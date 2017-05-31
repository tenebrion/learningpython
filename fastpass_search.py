"""
Creating a program to log into the my disney experience site and check for fastpass tickets

Example:
fastpass_search.py animal
fastpass_search.py magic
fastpass_search.py hollywood
fastpass_search.py epcot

Future version: Check for fastpass tickets. If there are tickets I want, try to add them to
my account. If there are issues, send a text message to me so I can login on my phone
and add them to my account.

Also in a future version: functions
"""
from selenium import webdriver
import time
from datetime import date
from datetime import timedelta
import sys

# Need to make sure we always search 30 days ahead. That is the limit for an annual pass holder
month_ahead = (date.today() + timedelta(days=30)).day  # setting future date to 30 days ahead
site_date_format = "//span[.='{}']".format(month_ahead)

# Setting up User / Password so that it loads prior to the browser opening
# this will be handled through a browser that 'saves the user and pass' so all it has to do is click login
USERNAME = input("Enter user: ")
PASSWORD = input("Enter password: ")

# Park URL's for fastpass selection (in XPATH format for web lookups)
animal_kingdom = "//img[@src='https://secure.parksandresorts.wdpromedia.com/resize/mwImage/1/462/90/75/" \
                 "wdpromedia.disney.go.com/media/wdpro-assets/my-magic-plus/fastpass-plus/" \
                 "vignettes/Vignette_Animal_Kingdom_4000x800-2.png?29032016145623']"

epcot = "//img[@src='https://secure.parksandresorts.wdpromedia.com/resize/mwImage/1/462/90/75/" \
        "wdpromedia.disney.go.com/media/wdpro-assets/my-magic-plus/fastpass-plus/" \
        "vignettes/Vignette_Epcot_4000x800-2.png?29032016145806']"

hollywood_studios = "//img[@src='https://secure.parksandresorts.wdpromedia.com/resize/mwImage/1/462/90/75/" \
                    "wdpromedia.disney.go.com/media/wdpro-assets//my-magic-plus/fastpass-plus/" \
                    "vignettes/Vignette_HollywoodStudios_4000x800-2.png?29032016150408']"

magic_kingdom = "//img[@src='https://secure.parksandresorts.wdpromedia.com/resize/mwImage/1/462/90/75/" \
                "wdpromedia.disney.go.com/media/wdpro-assets/my-magic-plus/fastpass-plus/" \
                "vignettes/Vignette_Magic_Kingdom_4000x800-2.png?29032016150619']"

park_pick = None
if len(sys.argv) >=1 :
    park_pick = str(sys.argv[1].lower())
    print(park_pick)


def park_selection(park):
    """
    
    :param park: 
    :return: 
    """
    if park == "animal":
        return animal_kingdom
    elif park == "epcot":
        return epcot
    elif park == "hollywood":
        return hollywood_studios
    elif park == "magic":
        return magic_kingdom


def site_searches(element, value):
    """
    
    :param element: 
    :param value: 
    :return: 
    """
    # this method will take an element and combine it with a value
    # the goal is to clean up the lines below
    if element == "xpath":
        pass
    elif element == "css":
        pass
    elif element == "id":
        pass
    elif element == "class":
        pass

# validating park selection
the_park = park_selection(park_pick)

# Loading Chrome and setting basic info.
chrome_driver = r"C:\Users\michael.f.koegel\Documents\Python\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver)
browser.get("https://disneyworld.disney.go.com/fastpass-plus/select-party/")

# setting up the log on process (User / Pass)
email_element = browser.find_element_by_id("loginPageUsername")
email_element.send_keys(USERNAME)
password_element = browser.find_element_by_id("loginPagePassword")
password_element.send_keys(PASSWORD)

# once the password is entered, we need to click on the Sign In button
click_password_link = browser.find_element_by_id("loginPageSubmitButton")
click_password_link.click()

time.sleep(5)  # need to take a quick nap
add_guests = browser.find_element_by_xpath("//span[.='Select All']")
add_guests.click()

click_next_fastpass = browser.find_element_by_xpath("//div[@class='button next primary']")
click_next_fastpass.click()

# clicking the next month option
time.sleep(5)
next_month = browser.find_element_by_css_selector("div.container.calendarContainer.ng-scope > "
                                                  "div > div > div.header > span.next-month")
next_month.click()

# selecting the date we need
next_month = browser.find_element_by_xpath(site_date_format)
next_month.click()

time.sleep(5)
select_park = browser.find_element_by_xpath(the_park)
select_park.click()
