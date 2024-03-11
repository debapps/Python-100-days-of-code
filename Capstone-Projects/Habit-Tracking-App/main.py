import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# This is Habit Tracking Application with Pixela API.

# Load the environment file.
load_dotenv()

# Constants.
USERNAME = 'debamckv'
USER_TOKEN = os.getenv('TOKEN')
URL = 'https://pixe.la'
GRAPH_ID = 'graph01'
HTTP_HEADER = {
    'X-USER-TOKEN': USER_TOKEN,
}

def call_pixel_api(URL, data = {}, method='POST', headers = {}):
    """This method calls the pixel api and prints the response message."""
    
    response = None

    if method == 'POST':
        response = requests.post(url=URL, json=data, headers=headers)
    elif method == 'PUT':
        response = requests.put(url=URL, json=data, headers=headers)
    elif method == 'DELETE':
        response = requests.delete(url=URL, headers=headers)
    else:
        response = requests.get(url=URL)
    
    if response.text:
        data = response.json()

        if data['isSuccess']:
            print(data['message'])
        else:
            print(f'\n ERROR: {data['message']}')
    else:
        print('\n ERROR: API Call issue.')

# Create pixela user account.
user_endpoint = f'{URL}/v1/users'
user_data = {
    'username': USERNAME,
    'token': USER_TOKEN,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# call_pixel_api(URL=user_endpoint, data=user_data)


# Creating a graph.
graph_endpoint = f'{URL}/v1/users/{USERNAME}/graphs'
graph_config = {
    'id': GRAPH_ID,
    'name': 'Reading Habit Graph',
    'unit': 'Pages',
    'type': 'int',
    'color': 'sora',
}

# call_pixel_api(URL=graph_endpoint, data=graph_config, headers=HTTP_HEADER)


# Create a pixel for today's data.
pixel_create_endpoint= f'{URL}/v1/users/{USERNAME}/graphs/{GRAPH_ID}'
today = datetime.now().strftime('%Y%m%d')
pixel_data = {
    'date': today,
    'quantity': input('\nEnter the number pages you read today: '),
}

call_pixel_api(URL=pixel_create_endpoint, data=pixel_data, headers=HTTP_HEADER)


# Update pixel data.
yesterday = datetime.now() - timedelta(days=1)
pixel_put_endpoint = f'{pixel_create_endpoint}/{yesterday.strftime('%Y%m%d')}'
# pixel_put_data = {
#     'quantity': input('\nEnter the updated number pages you read: '),
# }

# call_pixel_api(URL=pixel_put_endpoint, data=pixel_put_data, headers=HTTP_HEADER, method='PUT')


# Delete pixel data.
pixel_delete_endpoint = f'{pixel_create_endpoint}/{today}'

# call_pixel_api(URL=pixel_delete_endpoint, headers=HTTP_HEADER, method='DELETE')

# # response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# # print(response.text)

