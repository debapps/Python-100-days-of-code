from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep


# This program plays the Cookie Clicker Game (web url - https://orteil.dashnet.org/experiments/cookie/) 
# to maximize the "cookies/second" rate.
# It use selenium to create a bot that automatically plays the game for 5 minites.

# Constants.
URL = 'https://orteil.dashnet.org/experiments/cookie/'
GAME_TIME_LIMIT = 5 * 60

# Global Variables.
# Keep the browser open once the program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Create the driver from Chrome browser.
driver = webdriver.Chrome(options=chrome_options)

# Open the URL using driver.
driver.get(url=URL)

continue_game = True
start_time = datetime.now()
check_widget_time = start_time


def click_cookie():
    """This clicks on big cookie."""

    cookie = driver.find_element(By.ID, value='cookie')
    cookie.click()

def get_cookie_value(id):
    """This function gets the cookie value of the widget by id."""
    css_selector = f'#{id} b'
    value = driver.find_element(By.CSS_SELECTOR, value=css_selector).text
    cookie_value = int(value.split('-')[1].strip().replace(',', ''))
    return cookie_value

def get_cookie_score():
    """This function gets the cookie score."""
    score = int(driver.find_element(By.ID, value='money').text.replace(',', ''))
    return score

def click_widget_by_id(id):
    """This function clicks on widget based on ID."""
    widget = driver.find_element(By.ID, value=id)
    widget.click()
    # print(f'{id} is clicked.')

def check_widget():
    if get_cookie_score() >= get_cookie_value('buyFactory'):
        click_widget_by_id('buyFactory')
    elif get_cookie_score() >= get_cookie_value('buyGrandma'):
        click_widget_by_id('buyGrandma')
    elif get_cookie_score() >= get_cookie_value('buyCursor'):
        click_widget_by_id('buyCursor')


def show_cookie_rate():
    """This function print the cookies/second rate."""
    cookie_rate = driver.find_element(By.ID, value='cps').text
    print(cookie_rate)


while continue_game:
    click_cookie()

    check_widget_interval = datetime.now() - check_widget_time
    if check_widget_interval.total_seconds() >= 5:
        check_widget()
        check_widget_time = datetime.now()

    time_interval = datetime.now() - start_time
    if time_interval.total_seconds() >= GAME_TIME_LIMIT:
        continue_game = False
        show_cookie_rate()
        driver.quit()





