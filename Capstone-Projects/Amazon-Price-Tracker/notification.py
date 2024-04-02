# This module is responsible for sending email messages when the amazon product price is less than or
# equal to the target price.

import smtplib
from dotenv import load_dotenv
import os

# Load the environment file.
load_dotenv()

# Constants.
MAIL_HOST = 'smtp.gmail.com'
MAIL_PORT = 587
FROM_EMAIL = 'bhar.debaditya@gmail.com'
APP_PASS = os.getenv('APP_PASS_CODE')

class NotifyManager:

    def __init__(self, email) -> None:
        self.to_email = email

    def send_email(self, item, target_price, current_price, amazon_url):

        email_message = f'Subject: Amazon Price Alert for {item}!\n\n {item} is available at Rs. {current_price}/- only on Amazon.\nYour Target Price was Rs. {target_price}/-.\nHurry up and buy {item} using following link - \n{amazon_url}'
        
        # Create a SMTP connection.
        with smtplib.SMTP(host=MAIL_HOST, port=MAIL_PORT) as connection:
            # Put the connection to SMTP server into TLS mode.
            connection.starttls()

            # Login to the sender email.
            connection.login(user=FROM_EMAIL, password=APP_PASS)

            # Send the email.
            connection.sendmail(
                from_addr=FROM_EMAIL, 
                to_addrs=self.to_email, 
                msg=email_message
            )

# obj = NotifyManager('debadityabhar@icloud.com')
# obj.send_email('Harry Potter Books Set', 1300, 1298.50, 'https://amazon.in')
