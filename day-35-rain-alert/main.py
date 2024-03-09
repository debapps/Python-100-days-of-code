import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

# Description: This program checks the weather condition forcast data for the 24 hours and 
# sends SMS message to the specific user/phone number. It alerts if it is going to rain today 
# and ask to bring umbrella. It also informs if it is a sunny day.

# API used: 
# 1. Open Weather Map - For getting weather forcast data.
# 2. Twilio API - For sending sms. 

# Load the environment variable.
load_dotenv()

# Constants.
API_URL = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = os.getenv('OWM_API_KEY')
# MY_LAT = 52.348580
# MY_LON = -127.692200
MY_LAT = 22.7528
MY_LON = 88.3422
API_PARAMS = {
    'lat': MY_LAT,
    'lon': MY_LON,
    'units': 'metric',
    'cnt': 8,
    'appid': API_KEY,
}

def send_sms(to_number, msg):
    """This function send SMS message provided to the phone number provided."""

    account_sid = os.getenv('TWILIO_ACCNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=os.getenv('TWILIO_PHN_NUM'),
        body=msg,
        to=to_number
    )

    print(f'SMS is {message.status}')

def call_api(URL, params = {}):
    """This function calls API with its parameters."""
    response = requests.get(url=URL, params=params)
    response.raise_for_status()

    data = response.json()
    return data

# Get the weather forcast data for next 24 hours.
api_data = call_api(URL=API_URL, params=API_PARAMS)

# Format the API data.
forcast_data = api_data['list']
weather_data = [x['weather'] for x in forcast_data]
weather_cond_data = [x[0]['id'] for x in weather_data]

# Check if there is a possibility of rain/snow.
is_possible_rain = [id < 700 for id in weather_cond_data]

# If there is any possibilities of rain/swon bring umbrella.
if any(is_possible_rain):
    send_sms(to_number='+916290093829', msg='It\'s going to rain today. Remember to take ☔️')
else:
    send_sms(to_number='+916290093829', msg='Hope it\'s clear sky today. 🌤️ 🌕')

