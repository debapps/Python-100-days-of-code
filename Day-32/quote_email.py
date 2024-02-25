# Sending Email using Python Code. 
 
import smtplib
from random import choice
from dotenv import load_dotenv
import os

# Load the environment file.
load_dotenv()

# Constants.
FROM_EMAIL = 'bhar.debaditya@gmail.com'
APP_PASS = os.getenv('APP_PASS_CODE')
TO_EMAIL = 'debadityabhar@icloud.com'
MAIL_HOST = 'smtp.gmail.com'
MAIL_PORT = 587
QUOTE_FILE = 'quotes.txt'

# Get a random quote of the day from the QUOTE_FILE.
with open(QUOTE_FILE) as quote_file:
    quotes = quote_file.readlines()
    email_msg = choice(quotes)


# Create a SMTP connection.
with smtplib.SMTP(host=MAIL_HOST, port=MAIL_PORT) as connection:
    # Put the connection to SMTP server into TLS mode.
    connection.starttls()
    # Login to the sender email.
    connection.login(user=FROM_EMAIL, password=APP_PASS)
    # Send the email.
    connection.sendmail(
        from_addr=FROM_EMAIL, 
        to_addrs=TO_EMAIL, 
        msg=f'Subject: Quote of the Day from Python!\n\n{email_msg}'
    )


