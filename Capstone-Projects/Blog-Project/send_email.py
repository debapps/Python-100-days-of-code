import smtplib
from dotenv import load_dotenv
import os

# This module is responsible for sending email.

# Load the environment file.
load_dotenv()

# Constants.
FROM_EMAIL = 'bhar.debaditya@gmail.com'
APP_PASS = os.getenv('APP_PASS_CODE')
TO_EMAIL = 'debadityabhar@icloud.com'
MAIL_HOST = 'smtp.gmail.com'
MAIL_PORT = 587

class Email:

    def __init__(self, email_sub, email_msg) -> None:
        self.subject = email_sub
        self.message = email_msg

    def send_email(self):
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
                msg=f'Subject: {self.subject}\n\n{self.message}'
            )