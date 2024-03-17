import requests

SHEETY_API_URL = 'https://api.sheety.co/657940a50f966543d73748e105260d9b/cheapFlightDeals/prices'

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.sheet_data = None

    def read_sheet_data(self):
        """This function reads the google sheet data and returns it."""

        response = requests.get(url=SHEETY_API_URL)
        response.raise_for_status()
        self.sheet_data = response.json()['prices']
        return self.sheet_data
    
    def update_sheet_data(self, data_row):
        """This function updates a google sheet data row."""
        
        self.updated_data = {
            'price': data_row
        }
        self.update_url = f'{SHEETY_API_URL}/{data_row['id']}'
        response = requests.put(url=self.update_url, json=self.updated_data)
        response.raise_for_status()