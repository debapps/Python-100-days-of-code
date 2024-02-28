import requests
from datetime import datetime
import smtplib
from random import choice
from dotenv import load_dotenv
import os
from time import sleep

# Load the environment file.
load_dotenv()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# Constants.
ISS_URL = 'http://api.open-notify.org/iss-now.json'
SUN_URL = 'https://api.sunrise-sunset.org/json'
MY_LAT = 22.748501
MY_LONG = 88.320534
MY_TIMEZONE = 'Asia/Kolkata'
FROM_EMAIL = 'bhar.debaditya@gmail.com'
APP_PASS = os.getenv('APP_PASS_CODE')
TO_EMAIL = 'debadityabhar@icloud.com'
MAIL_HOST = 'smtp.gmail.com'
MAIL_PORT = 587
QUOTE_FILE = 'quotes.txt'


def call_api(url, params = {}):
    """This function calls the API and returns its response."""
    
    response = requests.get(url=url, params=params)
    response.raise_for_status()

    status = response.status_code
    data = None

    if status == 200:
        data = response.json()
        
    return data


# Sunrise Sunset API.
def check_sun_set():
    """This function checks if Sun is down."""
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'tzid': MY_TIMEZONE,
        'formatted': 0
    }

    data = call_api(url=SUN_URL, params=parameters)
    sunrise_time = datetime.strptime(data['results']['sunrise'], '%Y-%m-%dT%H:%M:%S+05:30') 
    sunset_time = datetime.strptime(data['results']['sunset'], '%Y-%m-%dT%H:%M:%S+05:30') 
    current_time = datetime.now()

    # print(f'Current Hour: {current_time.hour}')
    # print(f'Sunrise Hour: {sunrise_time.hour}')
    # print(f'Sunset Hour: {sunset_time.hour}')
    if current_time.hour < sunrise_time.hour and current_time.hour > sunset_time.hour:
        return True
    else:
        return False 

# ISS Tracker API.

def get_ISS_pos():
    """This function gets the ISS position."""

    data = call_api(url=ISS_URL)
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    iss_position = (longitude, latitude)
    return iss_position

def check_ISS_above_you():
    iss_pos = get_ISS_pos()

    if (
        iss_pos[0] >= MY_LONG - 5 and iss_pos[0] <= MY_LONG + 5
        ) or (
        iss_pos[1] >= MY_LAT - 5 and iss_pos[1] <= MY_LAT + 5    
        ):
        return True
    else:
        return False 


# Send Email.

def send_emai():
    """This function sends email message to the specific receiver."""
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
            msg=f'Subject: ISS Above You.\n\nLook Up!!'
        )
while True:
    print(f'\nCurrent Time: {datetime.now().time()}')
    print(f'SunSet?: {check_sun_set()}')
    print(f'Above Me?: {check_ISS_above_you()}')

    if check_sun_set() and check_ISS_above_you():
        send_emai()
    else:
        print(f'\nISS Position: {get_ISS_pos()}')

    sleep(60)
    