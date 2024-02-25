import smtplib
from datetime import date
from random import choice
from dotenv import load_dotenv
import os

# Send a motivational quote through Email on current weekday. (probably on Monday)

# Load the environment file.
load_dotenv()

# Constants.
SENDER_EMAIL = 'bhar.debaditya@gmail.com'
APP_PASS = os.getenv('APP_PASS_CODE')
RECIPIENT_EMAIL = 'debadityabhar@icloud.com'
MAIL_HOST = 'smtp.gmail.com'
MAIL_PORT = 587
QUOTE_FILE = 'quotes.txt'
WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_current_weekday():
    """This function currently get the day of the week of current date"""
    
    current_date = date.today()
    day_of_week = current_date.weekday()
    return WEEKDAYS[day_of_week]

def get_random_quote():
    """This function gets a random quote message from the quote file."""
    
    with open(QUOTE_FILE) as quote_file:
        quotes = quote_file.readlines()
        rand_quote_msg = choice(quotes)

    return rand_quote_msg

def send_email(message):
    """This function sends email to the recipient from the sender email. 
    The message to be send is the input."""
    
    with smtplib.SMTP(host=MAIL_HOST, port=MAIL_PORT) as connection:
        # Put the connection to SMTP server into TLS mode.
        connection.starttls()
        # Login to the sender email.
        connection.login(user=SENDER_EMAIL, password=APP_PASS)
        # Send the email.
        connection.sendmail(
            from_addr=SENDER_EMAIL, 
            to_addrs=RECIPIENT_EMAIL, 
            msg=f'Subject: Quote of the Day\n\n{message}'
        )

#-------------------------- Main Flow --------------------------#
if get_current_weekday() == 'Sunday':
    send_email(get_random_quote())