# This module is responsible to get the google sheet amazon product data.
# The data contains following fields: item, amazonUrl and targetPrice
# Data format: List of python dictionaries.

import requests

GOOGLE_SHEET_API = 'https://api.sheety.co/657940a50f966543d73748e105260d9b/amazonPriceTracker/amazonProducts'

class AmazonData:

    def __init__(self) -> None:
       response = requests.get(url=GOOGLE_SHEET_API)
       response.raise_for_status()
       self.sheet_data = response.json()

    def get_wishlist(self):
        """This function returns the Amazon Wishlist data in the google spreadsheet."""
        return self.sheet_data['amazonProducts']
    

# obj = AmazonData()
# print(obj.get_wishlist())