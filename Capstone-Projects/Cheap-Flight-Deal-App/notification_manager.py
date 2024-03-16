from twilio.rest import Client
from dotenv import load_dotenv
import os
from flight_data import FlightData

# Load the environment file.
load_dotenv()

# Constants
ACCNT_SID = os.getenv('TWILIO_ACCNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self, phone_number, flight_data: FlightData) -> None:
        self.client = Client(ACCNT_SID, AUTH_TOKEN)
        self.to_number = phone_number
        self.sms_body = f'Low Price Alert!! Only Rs. {flight_data.get_price()}/- to fly from {flight_data.get_org_city()} - {flight_data.get_org_code()} to {flight_data.get_dest_city()} - {flight_data.get_dest_code()} \
                        from {flight_data.get_out_date()} to {flight_data.get_in_date()}.'
    
    def send_sms(self):
        """This function send SMS message provided to the phone number provided."""

        message = self.client.messages.create(
            from_=os.getenv('TWILIO_PHN_NUM'),
            body=self.sms_body,
            to=self.to_number
        )

        print(f'SMS is {message.status}')