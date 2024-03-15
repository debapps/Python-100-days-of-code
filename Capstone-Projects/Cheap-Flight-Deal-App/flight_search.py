import requests
from dotenv import load_dotenv
import os

# Load the environment file.
load_dotenv()

# Constants
FLIGHT_SEARCH_HOST = 'https://api.tequila.kiwi.com'
FLIGHT_SEARCH_KEY = os.getenv('FLIGHT_SEARCH_API_KEY')
LOC_API_ENDPOINT = '/locations/query'
API_HEADER = {
    'apikey': FLIGHT_SEARCH_KEY
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    
    def get_iata_code(self, city_name):
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
    
