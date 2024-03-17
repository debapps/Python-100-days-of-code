import requests

SHEETY_USER_ENDPOINT = 'https://api.sheety.co/657940a50f966543d73748e105260d9b/cheapFlightDeals/users'

class UserData:

    # This class represents the user specific data.

    def __init__(self) -> None:
        response = requests.get(url=SHEETY_USER_ENDPOINT)
        response.raise_for_status()
        self.user_data = response.json()['users']

    def get_users(self):
        self.users = [(user['firstName'], user['email']) for user in self.user_data]
        return self.users



