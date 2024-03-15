import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# Load the environment file.
load_dotenv()

# Constants.
FLIGHT_SEARCH_API_HOST = 'https://api.tequila.kiwi.com/v2'
FLIGHT_SEARCH_KEY = os.getenv('FLIGHT_SEARCH_API_KEY')
API_HEADER = {
    'apikey': FLIGHT_SEARCH_KEY
}
SEARCH_ENDPOINT = '/search'

class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, departure_city, departure_airport_code, currency):
        self.departure_city = departure_city
        self.departure_airport_code = departure_airport_code
        self.currency = currency
        tomorrow = datetime.now() + timedelta(days=1)
        day_after_six_month = datetime.now() + timedelta(days=180)
        self.journey_dates = [tomorrow.strftime('%d/%m/%Y'), day_after_six_month.strftime('%d/%m/%Y')]


    def search_cheap_flight(self, dest_city_code):
        flight_search_url = f'{FLIGHT_SEARCH_API_HOST}{SEARCH_ENDPOINT}'
        flight_parameters = {
            'fly_from': self.departure_airport_code,
            'fly_to': dest_city_code,
            'curr': self.currency,
            'date_from': self.journey_dates[0],
            'date_to': self.journey_dates[1],
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'ret_from_diff_city': False,
            'ret_to_diff_city': False,
            'adults': 1,
            'selected_cabins': 'M',
            'adult_hold_bag': '1',
            'adult_hand_bag': '1',
            'locale': 'en',
            'limit': 100
        }

        response = requests.get(url=flight_search_url, headers=API_HEADER, params=flight_parameters)
        response.raise_for_status()
        self.flight_data = response.json()['data'][0]
        

        # Format the flight data.
        price = self.flight_data['price']
        arrival_city = self.flight_data['cityTo']
        arrival_city_iata_code = self.flight_data['flyTo']
        outbound_date = self.flight_data['local_departure'].split('T')[0]
        route_data = self.flight_data['route']
        for route in route_data:
            if route['flyFrom'] == arrival_city_iata_code:
                inbound_date = route['local_departure'].split('T')[0]

        self.formatted_flight_data = {
            'departure_city': self.departure_city,
            'departure_city_iata_code': self.departure_airport_code,
            'arrival_city': arrival_city,
            'arrival_city_iata_code': arrival_city_iata_code,
            'price': price,
            'outbound_date': outbound_date,
            'inbound_date': inbound_date
        }

        return self.formatted_flight_data

    

