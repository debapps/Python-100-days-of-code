from selenium import webdriver
from selenium.webdriver.common.by import By

# Constants
GOOGLE_FORM_URL = 'https://forms.gle/XK4nj9vQyJbvwUMV8'
ADDRESS_INPUT_CSS = '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input'
PRICE_INPUT_CSS =  '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input'
LINK_INPUT_CSS = '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input'
SUBMIT_CSS = '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div'

class GoogleFormInput:

    def __init__(self) -> None:
        # Keep the browser open once the program finishes.
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)

        # Create the driver from Chrome browser.
        self.driver = webdriver.Chrome(options=chrome_options)

        # Open the URL using driver and wait for 2 seconds.
        self.driver.get(url=GOOGLE_FORM_URL)

    def input_address(self, address):
        # Get the address input field.
        addr_input = self.driver.find_element(By.CSS_SELECTOR, value=ADDRESS_INPUT_CSS)

        # input the value.
        addr_input.send_keys(address)

    def input_price(self, price):
        # Get the price input field.
        price_input = self.driver.find_element(By.CSS_SELECTOR, value=PRICE_INPUT_CSS)

        # input the value.
        price_input.send_keys(price)

    def input_zillow_link(self, link):
        # Get the link input field.
        link_input = self.driver.find_element(By.CSS_SELECTOR, value=LINK_INPUT_CSS)

        # input the value.
        link_input.send_keys(link)

    def submit_form(self):
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, value=SUBMIT_CSS)
        submit_btn.click()

    def close_browser(self):
        self.driver.quit()
