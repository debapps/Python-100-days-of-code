# This module is responsible for the scraping the Amazon product page and get the current price.

from bs4 import BeautifulSoup
import requests

class AmazonPriceScrape:

    def __init__(self, url) -> None:
        self.web_url = url
        self.header = {
            'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        }

        response = requests.get(url=self.web_url, headers=self.header)
        response.raise_for_status()
        self.web_content = response.text

    def get_price(self):
        try:
            soup = BeautifulSoup(self.web_content, 'html.parser')
            price_element = soup.select_one('span.a-offscreen')
            price_str = price_element.string.split('₹')[1].replace(',', '')
            return float(price_str)
        except:
            print('Web Scraping Error')
            return 0
        


# obj = AmazonPriceScrape('https://www.amazon.in/Tintin-Collection-Adventure-Adventures-Editions/dp/1405278455/ref=sr_1_1?crid=3VEAHEEWZ6X35&dib=eyJ2IjoiMSJ9.Z4W3JZIuqOsIXaeItbK3MOqUD3BPzQ5iIH4MdiA4YspiatDZ2RwrDbqARQARqqDJ7qz4YBTx4tlFzJEdKN5zvgJmmhd2RUiqM4EZnhFsTQa9F3cYmvFf6KB3w-rouEPrvuuPrhzvGBJn1F5L9-cSG7LjPV2ixmTln8RbzcfS6z_GPuYBCkcV7Kj2tZziZMrB60PASkR1Z8Z674lK1Zwt6loFZGwZPT-iB8G6BaVRzfk.h2DPkbpA7jpqSMo4mkIWldSgIpWUFMUYssySXvJL5Q8&dib_tag=se&keywords=tintin+books+set&psr=EY17&qid=1711985943&s=todays-deals&sprefix=tintin+books+set%2Ctodays-deals%2C230&sr=1-1')
# print(obj.get_price())
