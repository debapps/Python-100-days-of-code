from dotenv import load_dotenv
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException

# This program is the instagram follower bot. It uses selenium webdriver to perform the following tasks:
# 1. It login to your instagram account. 
# 2. Search for the target account.
# 3. Find all the followers of the target account.
# 4. Follow all the followers.

# Load the environment variables.
load_dotenv()

# Constants
URL_STRING = 'https://www.instagram.com/' 
EMAIL = os.getenv('MY_LOGIN_EMAIL')
PASSWORD = os.getenv('MY_LOGIN_PASSWORD')
TARGET_ACCNT = 'javascript.js'
ACCNT_FOLLOWER_URL = f'{URL_STRING}{TARGET_ACCNT}/followers'

class InstaFollower:

    def __init__(self) -> None:
        # Keep the browser open once the program finishes.
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)

        # Create the driver from Chrome browser.
        self.driver = webdriver.Chrome(options=chrome_options)

        # Open the URL using driver.
        self.driver.get(url=URL_STRING)

        # Wait for 30 second.
        self.driver.implicitly_wait(30)

    
    def login(self):
        """This function login to instagram account using facebook."""
        # Click on the button "Log in with Facebook".
        click_facebook = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[5]/button/span[2]')
        click_facebook.click()

        # Get the form elements.
        email_textbox = self.driver.find_element(By.NAME, value='email')
        password_textbox = self.driver.find_element(By.NAME, value='pass')
        login_btn= self.driver.find_element(By.ID, value='loginbutton')

        # Set the form values.
        email_textbox.send_keys(EMAIL)
        password_textbox.send_keys(PASSWORD)

        # Submit the form.
        login_btn.click()

        # Wait for 30 second.
        self.driver.implicitly_wait(30)

        # Click on the notification button.
        try:
            self.driver.find_element(By.XPATH, value='//button[contains(text(), "Not Now")]').click()
        except WebDriverException: 
            print('ERROR: Web driver exception. func: login()')

    def find_followers(self):
        "This function go to the target account page and click on follower." 

        self.driver.get(url=ACCNT_FOLLOWER_URL)

        # Get number of followers.
        follower_link_xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span'
        followers = int(self.driver.find_element(By.XPATH, value=follower_link_xpath).get_attribute('title').replace(',', ''))
        
        print(f'Followers: {followers}')

        sleep(8.2)
        # find the modal element xpath.
        modal_xpath = '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]'
        modal = self.driver.find_element(By.XPATH, value=modal_xpath)

        # Scroll through entire modal
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            # self.driver.implicitly_wait(2)
            sleep(2)

    def follow(self):
        pass
    


if __name__ == '__main__':

    insta = InstaFollower()

    insta.login()
    insta.find_followers()



