from selenium import webdriver
from selenium.webdriver.common.by import By

# Constants.
URL = 'https://www.amazon.in/Noise-Wireless-Earbuds-Playtime-Instacharge/dp/B0C7L4MY51/ref=sr_1_1_sspa?crid=1OFOELPYSEYP0&dib=eyJ2IjoiMSJ9.45DxgjpQKo3wnWBYQa0KQ0LL65mTV1eP0bYhE3pKyH5gr7GsdKKeDgjL01buZdqwFOIxjcuObaYzcX_mliUx1fSdpy96vYEgSgXyZIu4m6vLLCYRp1HXuHQOcmf0ggJ36Dv0KQUrRACY6l3lHmuN0B4b6UV3Ht2P0mDu_xiBli0E4VxjswqOj902Ggq_KUDk5CamFNNSorW9KrdU4oaAwPvxqL0mXu_gyGOSezgrp04.5Jpg7UQRhPKVksSNzv-VfvrwgIutRdWYYtijGUagthc&dib_tag=se&keywords=noise+earbuds&qid=1713363694&sprefix=noise%2Caps%2C245&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

# Keep the browser open once the program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Create the driver from Chrome browser.
driver = webdriver.Chrome(options=chrome_options)

# Open the URL using driver.
driver.get(url=URL)

# Get the product title and price from Amazon using ID and Class Name locators.
product_title = driver.find_element(By.ID, value='productTitle').text
product_price = driver.find_element(By.CLASS_NAME, value='a-price-whole').text

# Get element by XPATH.
discount = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]').text

# Get the search bar by name and search button by ID.
search_bar = driver.find_element(By.NAME, value='field-keywords')
placehoder = search_bar.get_attribute('placeholder')
search_btn = driver.find_element(By.ID, value='nav-search-submit-button')

# Get element by CSS selectors.
amazon_sell_link = driver.find_element(By.CSS_SELECTOR, value='#navFooter > div.navFooterVerticalColumn.navAccessibility > div > div:nth-child(5) > ul > li.nav_first > a')

# Display Output.
print('\nAmazon Product Price Info')
print(f'\nProduct - {product_title}\nPrice - Rs. {product_price}/- Discount - {discount}\n')
print(search_bar)
print(placehoder)
print(search_btn.tag_name, search_btn.get_attribute('type'))
print(amazon_sell_link.text)

# Close the browser.
# close() method closes the active tab.
# driver.close()
# quit() method closes the entire browser
driver.quit()