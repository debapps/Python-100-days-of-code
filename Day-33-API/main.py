import requests
import datetime

def call_api(url, params = {}):
    """This function calls the API and returns its response."""
    
    response = requests.get(url=url, params=params)
    response.raise_for_status()

    status = response.status_code
    data = None

    if status == 200:
        data = response.json()
        
    return data

# ISS Tracker API.
# URL = 'http://api.open-notify.org/iss-now.json'

# data = call_api(url=URL)
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
# iss_position = (longitude, latitude)

# print(f'Response Body:\n {data}')
# print(f'\nISS Position: {iss_position}')

# Sunrise Sunset API.
URL = 'https://api.sunrise-sunset.org/json'
MY_LAT = 22.748501
MY_LONG = 88.320534
MY_TIMEZONE = 'Asia/Kolkata'

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'tzid': MY_TIMEZONE,
    'formatted': 0
}

data = call_api(url=URL, params=parameters)
sunrise_time = datetime.datetime.strptime(data['results']['sunrise'], '%Y-%m-%dT%H:%M:%S+05:30') 
sunset_time = datetime.datetime.strptime(data['results']['sunset'], '%Y-%m-%dT%H:%M:%S+05:30') 
current_time = datetime.datetime.now()

print(f'Current Time: {current_time}')
print(f'Sunrise Time: {sunrise_time}')
print(f'Sunset Time: {sunset_time}')
