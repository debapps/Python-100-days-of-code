from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from user_data import UserData
from datetime import datetime, timedelta

# Constants
YOUR_CITY_IATA_CODE = 'CCU'
YOUR_PHN_NUM = '+916290093829'

# Get the data from google sheet.
data_manager = DataManager()
sheet_data = data_manager.read_sheet_data()

 # Get the user data for email ids.
user_data = UserData()
users = user_data.get_users()

# For all the row in the google sheet, Get the IATA Codes for a City code, if missing.
for row in sheet_data:
    flight_search = FlightSearch()

    if len(row['iataCode']) == 0:    
        row['iataCode'] = flight_search.get_iata_code(row['city'])
        data_manager.update_sheet_data(row)
        
    # Search the cheapest flights from your city to the destination city in the google sheet.
    tomorrow = datetime.now() + timedelta(days=1)
    day_after_six_months = datetime.now() + timedelta(days=(6 * 30))

    flight = flight_search.check_flights(YOUR_CITY_IATA_CODE, row['iataCode'], tomorrow, day_after_six_months)

    if flight == None:
        continue 

    # Check if the destination has the low price today than the price on the google sheet.
    if flight.get_price() < row['lowestPrice']:
        print(f'{flight.get_dest_city()} - Rs.{flight.get_price()} Only.')

        # Update the google sheet with today's lowest price.
        row['lowestPrice'] = flight.get_price()
        data_manager.update_sheet_data(row)

        # Notify the user by sending emails for all the email ids.
        notify = NotificationManager(flight)
        
        for (name, email) in users:
            notify.send_email(email, name)


