import requests

URL = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url=URL)
response.raise_for_status()

status = response.status_code
data = response.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position = (longitude, latitude)

print(f'Response status: {status}')
print(f'Response Body:\n {data}')
print(f'\nISS Position: {iss_position}')
