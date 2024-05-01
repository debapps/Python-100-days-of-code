# This is data entry automation project. It will webscrape the rental price and address of the
# houses in SanFransisco, CA and put the information into a Google form to gather all the rental
# data. The website we will scrape for rental information is the Zillow clone. 
# Zillow Clone - https://appbrewery.github.io/Zillow-Clone/
# Google Form - https://forms.gle/BvcTy5MQr62wUog9A

from rent_listing import RentList
from google_form_input import GoogleFormInput
from time import sleep


# Get the rent address, prices and zillow links.
rent = RentList()
rent_addresses = rent.get_rent_address()
rent_prices = rent.get_rent_prices()
zillow_links = rent.get_zillow_links()
total_listings = rent.get_listing_count()

print(f'\n Total Listing Counts = {total_listings}')

for idx in range(total_listings):
    # Create a google form interaction object.
    form = GoogleFormInput()

    # Sleep the process.
    sleep(5)

    # Input the rent address, price and zillow link values.
    form.input_address(rent_addresses[idx])
    form.input_price(rent_prices[idx])
    form.input_zillow_link(zillow_links[idx])

    # Submit the form.
    form.submit_form()

    # Close the form.
    form.close_browser()

    print(f'Record No - {idx + 1} is added to Google Form.')

print('\nAll records are added into the Google Form!')















