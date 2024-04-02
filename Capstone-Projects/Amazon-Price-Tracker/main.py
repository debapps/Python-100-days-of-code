# Automated Amazon Price Tracker.
# This program get the user wishlist from a google sheet. Scape the products from the wishlist from Amazon to
# get the current price of the product. If the current price is less than or equal to the traget price in
# the wishlist, notify user in his email to purchase the product.

# TODO #1 - Get the user whishlist.
from amazon_data_manager import AmazonData

amazon_wishlist = AmazonData()
wishlist = amazon_wishlist.get_wishlist()

# TODO #2 - Get the current prices of the products in the wishlist from Amazon.
from amazon_price_scrape import AmazonPriceScrape

product_data = []

for product in wishlist:
    amazon_scrape = AmazonPriceScrape(url=product['amazonUrl'])
    current_price = amazon_scrape.get_price()

    complete_price_data = {
        'item': product['item'],
        'amazonUrl': product['amazonUrl'],
        'targetPrice': product['targetPrice'],
        'currentPrice': current_price,
    }
    product_data.append(complete_price_data)


# TODO #3 - If the current price is less than the target price set by the user, 
# send buy notification email to user.
from notification import NotifyManager

TO_EMAIL = 'debadityabhar@icloud.com'

notify = NotifyManager(TO_EMAIL)

for product in product_data:
    if product['currentPrice'] <= product['targetPrice']:
        print(f'Low Price for {product['item']}')
        notify.send_email(product['item'], product['targetPrice'], product['currentPrice'], product['amazonUrl'])

