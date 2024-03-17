import requests
from dotenv import load_dotenv
import os
from flight_data import FlightData

# Load the environment file.
load_dotenv()

# Constants
FLIGHT_SEARCH_HOST = 'https://api.tequila.kiwi.com'
FLIGHT_SEARCH_KEY = os.getenv('FLIGHT_SEARCH_API_KEY')
API_HEADER = {
    'apikey': FLIGHT_SEARCH_KEY
}
LOC_API_ENDPOINT = '/locations/query'
SEARCH_ENDPOINT = '/v2/search'


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.currency = 'INR'
    
    def get_iata_code(self, city_name):
        """This function returns IATA code for a given city name."""

        location_url = f'{FLIGHT_SEARCH_HOST}{LOC_API_ENDPOINT}'

        location_parameters = {
            'locale': 'en-US',
            'location_types': 'city',
            'limit': 10,
            'active_only': True,
            'sort': 'name',
            'term': city_name,  
        }

        response = requests.get(url=location_url, headers=API_HEADER, params=location_parameters)
        response.raise_for_status()
        location = response.json()['locations'][0]
        code = location['code']
        return code 
    
    def check_flights(self, origin_city_code, destination_city_code, from_date, to_date):
        """This function checks round trip flights between given origin city and destination city on 
        given range of date."""

        flight_search_url = f'{FLIGHT_SEARCH_HOST}{SEARCH_ENDPOINT}'
        flight_parameters = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'curr': self.currency,
            'date_from': from_date.strftime('%d/%m/%Y'),
            'date_to': to_date.strftime('%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            # "flight_type": "round",
            'ret_from_diff_city': False,
            'ret_to_diff_city': False,
            'adults': 1,
            'selected_cabins': 'M',
            'adult_hold_bag': '1',
            'adult_hand_bag': '1',
            'locale': 'en',
            'limit': 20
        }

        response = requests.get(url=flight_search_url, headers=API_HEADER, params=flight_parameters)
        response.raise_for_status()

        try:
            flight_data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        
        # Format the flight data.
        out_date = flight_data['local_departure'].split('T')[0]

        in_date = ' '
        for route in flight_data['route']:
            if route['flyFrom'] == destination_city_code:
                in_date = route['local_departure'].split('T')[0] 

        
        flight_info = FlightData(
            price = flight_data['price'],
            origin_city = flight_data['cityFrom'],
            origin_city_code = flight_data['flyFrom'],
            destination_city = flight_data['cityTo'],
            destination_city_code = flight_data['flyTo'],
            outbound_date = out_date,
            inbound_date = in_date 
        )

        return flight_info
