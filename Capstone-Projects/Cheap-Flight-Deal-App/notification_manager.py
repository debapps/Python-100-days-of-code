from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load the environment file.
load_dotenv()

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self, phone_number, cheap_flight_data) -> None:
        self.to_number = phone_number
        self.sms_body = f'Low Price Alert!! Only Rs. {cheap_flight_data['price']}/- to fly from {cheap_flight_data['departure_city']} - {cheap_flight_data['departure_city_iata_code']} to {cheap_flight_data['arrival_city']} - {cheap_flight_data['arrival_city_iata_code']} from {cheap_flight_data['outbound_date']} to {cheap_flight_data['inbound_date']}.'
    
    def send_sms(self):
        """This function send SMS message provided to the phone number provided."""

        account_sid = os.getenv('TWILIO_ACCNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_=os.getenv('TWILIO_PHN_NUM'),
            body=self.sms_body,
            to=self.to_number
        )

        print(f'SMS is {message.status}')