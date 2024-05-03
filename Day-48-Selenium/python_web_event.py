from selenium import webdriver
from selenium.webdriver.common.by import By

# This program list out all the upcoming events from https://www.python.org/ web page 
# into a python dictionary.

# Constant.
URL = 'https://www.python.org/'

# Create the webdriver.
driver = webdriver.Chrome()

# Open the URL using driver.
driver.get(url=URL)

# Get the upcoming event elements.
upcoming_event_elements = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

# Creating upcoming event dictionary.
upcoming_event_dict = {}
for idx, event in enumerate(upcoming_event_elements):
    event_info = event.text.split('\n')
    event_date = event_info[0]
    event_title = event_info[1]
    event_dict = {
        'time': event_date,
        'name': event_title,
    }

    upcoming_event_dict[idx] = event_dict

print(upcoming_event_dict)


