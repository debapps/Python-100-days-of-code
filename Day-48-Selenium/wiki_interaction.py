from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# This program interacts with wikipedia main page - https://en.wikipedia.org/wiki/Main_Page

# Constant.
URL = 'https://en.wikipedia.org/wiki/Main_Page'

# Keep the browser open once the program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Create the driver from Chrome browser.
driver = webdriver.Chrome(options=chrome_options)

# Open the URL using driver.
driver.get(url=URL)

num_of_articles = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')

# Click on link.
# num_of_articles.click()

# Get the anchor tag (link) by link text.
comm_portal = driver.find_element(By.LINK_TEXT, value='Community portal')
# comm_portal.click()

# Get the input serach bar and type something in it, then press enter key.
search_bar = driver.find_element(By.NAME, value='search')
search_bar.send_keys('Python', Keys.ENTER)