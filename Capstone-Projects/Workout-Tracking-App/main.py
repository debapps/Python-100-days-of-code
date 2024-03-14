from dotenv import load_dotenv
import os
import requests
from datetime import datetime

# Load the environment file.
load_dotenv()

def api_post_call(url, data, header={}):
    response = requests.post(url=url, headers=header, json=data)
    response.raise_for_status()
    return response.json()

# Constants.
SHEETY_ENDPOINT_URL = 'https://api.sheety.co/657940a50f966543d73748e105260d9b/workoutTrackingApp/workouts'
API_HOST = 'https://trackapi.nutritionix.com'
ENDPOINT = '/v2/natural/exercise'
NUTRITIONIX_URL = f'{API_HOST}{ENDPOINT}'
APP_ID = os.getenv('NUTRITIONIX_API_APP_ID')
APP_KEY = os.getenv('NUTRITIONIX_API_KEY')
API_HEADER = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
    'x-remote-user-id': '0',
}

# Data for Nutritionix API.
payload = {
    'query': input('\nTell me the workouts you\'ve done for today:\n'),
    'weight_kg': 85,
    'height_cm': 180.34,
    'age': 35,
}

# Call the nutritionix api.
data = api_post_call(url=NUTRITIONIX_URL, data=payload, header=API_HEADER)


# Generate the google spreadsheet data to write into the sheet.
for workout in data['exercises']:
    google_sheet_row = {
        'workout': 
            {
                'date': datetime.now().strftime('%d/%m/%Y'),
                'time': datetime.now().strftime('%X'),
                'exercise': workout['name'].title(),
                'duration': int(workout['duration_min']),
                'calories': float(workout['nf_calories']),
            } 
    }

    # Save the data into google sheet using post API call.
    res = api_post_call(url=SHEETY_ENDPOINT_URL, data=google_sheet_row)
    print(res)




