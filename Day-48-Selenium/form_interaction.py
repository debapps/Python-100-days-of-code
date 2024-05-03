from selenium import webdriver
from selenium.webdriver.common.by import By

# This program goes to the below URL and fill the form (fisrt name, Last name and email address)
# and click the sign up button.

# URL
URL = 'https://secure-retreat-92358.herokuapp.com/'

# Keep the browser open once the program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Create the driver from Chrome browser.
driver = webdriver.Chrome(options=chrome_options)

# Open the URL using driver.
driver.get(url=URL)

# Get all the form elements.
fname_elem = driver.find_element(By.NAME, value='fName')
lname_elem = driver.find_element(By.NAME, value='lName')
email_elem = driver.find_element(By.NAME, value='email')
signup_btn = driver.find_element(By.CLASS_NAME, value='btn')

# Get all the input from user.
first_name = input('\nEnter Your First Name:\n')
last_name = input('\nEnter Your Last Name:\n')
email = input('\nEnter Your Email Address:\n')

# Place the data into form element.
fname_elem.send_keys(first_name)
lname_elem.send_keys(last_name)
email_elem.send_keys(email)

# Click the Sign Up Button.
signup_btn.click()

