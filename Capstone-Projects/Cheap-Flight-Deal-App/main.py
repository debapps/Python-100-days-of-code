from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# Constants
YOUR_CITY_NAME = 'Kolkata'
YOUR_CITY_IATA_CODE = 'CCU'
YOUR_CURRENCY = 'INR'
YOUR_PHN_NUM = '+916290093829'

# Get the data from google sheet.
data_manager = DataManager()
sheet_data = data_manager.read_sheet_data()

# For all the row in the google sheet, Get the IATA Codes for a City code, if missing.
for row in sheet_data:
    if len(row['iataCode']) == 0:
        flight_search = FlightSearch()
        row['iataCode'] = flight_search.get_iata_code(row['city'])
        data_manager.update_sheet_data(row)

    # Search the cheapest flights from your city to the destination city in the google sheet.
    flight = FlightData(YOUR_CITY_NAME, YOUR_CITY_IATA_CODE, YOUR_CURRENCY)
    cheap_flight_data = flight.search_cheap_flight(row['iataCode'])

    # Check if the destination has the low price today than the price on the google sheet.
    if cheap_flight_data['price'] < row['lowestPrice']:
        print(f'{cheap_flight_data['arrival_city']} - Rs.{cheap_flight_data['price']} Only.')

        # Update the google sheet with today's lowest price.
        row['lowestPrice'] = cheap_flight_data['price']
        data_manager.update_sheet_data(row)

        # Notify the user by sending SMS.
        notify = NotificationManager(YOUR_PHN_NUM, cheap_flight_data)
        notify.send_sms()


