import requests
from bs4 import BeautifulSoup

# Constants
ZILLOW_URL = 'https://appbrewery.github.io/Zillow-Clone/'
HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

class RentList:

    def __init__(self) -> None:
        # Get the content of the web page.
        response = requests.get(ZILLOW_URL, headers=HEADER)
        response.raise_for_status()
        zillow_web_content = response.text

        # Create the soup with the web content.
        zillow_soup = BeautifulSoup(zillow_web_content, 'html.parser')

        # Get list of rent listings.
        self.rent_listing = zillow_soup.css.select('li.ListItem-c11n-8-84-3-StyledListCardWrapper')

    def get_listing_count(self):
        return len(self.rent_listing)
    
    def get_rent_address(self):
        address_list = [item.a.get_text().strip().replace('|', '')
                       for item in self.rent_listing]
        return address_list
    
    def get_rent_prices(self):
        rent_prices = [item.span.get_text().split('+')[0].split('/')[0] 
                       for item in self.rent_listing]
        return rent_prices
    
    def get_zillow_links(self):
        zillow_links = [item.a.get('href') 
                       for item in self.rent_listing]
        return zillow_links