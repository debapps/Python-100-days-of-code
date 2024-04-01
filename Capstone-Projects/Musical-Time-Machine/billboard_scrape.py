import requests
from bs4 import BeautifulSoup
from datetime import datetime

# This script is responsible to scape website - billboad.com for the list of hot 100 songs for the 
# day user entered.

# Constants.
BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100/' 

class BillBoard:

    def __init__(self, date) -> None:
        self.songs = []
        
        # Create the url of the billboard webpage.
        self.billboad_web_page = f'{BILLBOARD_URL}{date}'


    def get_songs(self):
        # Get the constent of the web page.
        response = requests.get(url=self.billboad_web_page)
        response.raise_for_status()
        billboad_web_content = response.text

        # Create the soup.
        billboard_soup = BeautifulSoup(billboad_web_content, 'html.parser')

        # Get the list of all songs records.
        song_records = billboard_soup.select('.o-chart-results-list-row-container')

        # Get the titles of all 100 songs.
        for song in song_records:
            song_list_tag = song.select_one('ul > li.lrv-u-width-100p')

            song_title = song_list_tag.find(name='h3', class_='c-title').get_text().strip()
            self.songs.append(song_title)

        return self.songs
        
