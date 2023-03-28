# Written By Clarence Jiang, Please do not uncomment my authorship
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""
First step is log in into Linkedin
"""
# create webdriver, this line run significantly slow
driver = webdriver.Chrome("./chromedriver_mac64/chromedriver")
# go to linkedin login
driver.get("https://linkedin.com/uas/login")
# give the system more waiting time to make sure LinkedIn could be loaded successfully
time.sleep(5)

# find username position
username = driver.find_element(By.ID, "username")
# retrieve private info, username and password
username_value = os.environ["username"]
pw_value = os.environ["password"]

# send private username
username.send_keys(username_value)

# find password position and send private password
pword = driver.find_element(By.ID, "password")
pword.send_keys(pw_value)

# press enter
pword.send_keys(Keys.ENTER)

# # optional code used to stop the web
# input("Press Enter to quit")


"""
Second step: search for a target company name
"""
interested_company = os.environ["profile"]
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'search-global-typeahead__input')))

# Find the search box and enter the search term
search_box.send_keys(interested_company)
search_box.send_keys(Keys.ENTER)

# Wait for the search results to load
time.sleep(3)

"""
Third step: Click on the "View Page" button for the first search result
"""

view_page_button = driver.find_element(By.XPATH, '//span[text()="View page"]/..')
view_page_button.click()

# Wait for the company page to load
time.sleep(5)





