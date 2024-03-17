import os
from dotenv import load_dotenv
import smtplib
from flight_data import FlightData

# Load the environment file.
load_dotenv()

FROM_EMAIL = 'bhar.debaditya@gmail.com'
APP_PASS = os.getenv('APP_PASS_CODE')
MAIL_HOST = 'smtp.gmail.com'
MAIL_PORT = 587

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    
    def __init__(self, flight_data: FlightData):
        # Create a SMTP connection.
        self.connection = smtplib.SMTP(host=MAIL_HOST, port=MAIL_PORT)

        # Put the connection to SMTP server into TLS mode.
        self.connection.starttls()

        # Login to the sender email.
        self.connection.login(user=FROM_EMAIL, password=APP_PASS)

        # Email Message.
        self.email_message = f'\tOnly at Rs. {flight_data.get_price()}/- \n\
        For your dream destination - {flight_data.get_dest_city()} - {flight_data.get_dest_code()} \n\
        Starting from {flight_data.get_org_city()} - {flight_data.get_org_code()} \n\
        Journey Start Date - {flight_data.get_out_date()} \n\
        Return Date - {flight_data.get_in_date()} \n\n\
        For more updates, Join Bittu\'s Flight Club.'

    def close_connection(self):
        self.connection.close()

    def send_email(self, to_email, to_name):
        # Send the email.
        self.connection.sendmail(
            from_addr=FROM_EMAIL, 
            to_addrs=to_email, 
            msg=f'Subject: Low Flight Price Alert!!\n\nHello {to_name},\n\nThere are cheap flight deals for you today. Grab the opportunity to get round trip flights at low price.\n{self.email_message}'
        )