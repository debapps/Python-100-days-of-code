# This project is about musical time machine. The user is asked for a date. The website - billboad.com
# lists out 100 hot song for a week. The program perform webscraping 100 hot songs for the user entered
# date from the billboad webpage. Then the program uses spotify API to create a playlist of those songs.

from user_input_handler import UserInputHandler
from billboard_scrape import BillBoard 
from spotify_handler import SpotifyHandler

# Constants.
SPOTIFY_PLAYLIST_DESC = 'The hot 100 songs from BillBoard by time machine.'

# Welcome to the application.
print('\n\tMusical Time Machine: Create your own hot spotify playlist of past.\n')

# Get the user input date.
user_input = UserInputHandler() 
date = user_input.get_user_date()
spotify_playlist_name = f'BillBoard Hot 100 Songs: Dt. {date}'

# Get the 100 hot songs from a given date by scraping billboard webpage.
billboard = BillBoard(date)
songs = billboard.get_songs()

# Get the spotify object. Create spotify playlist and add the songs.
spotify = SpotifyHandler()
playlist = spotify.create_playlist(name=spotify_playlist_name, desc=SPOTIFY_PLAYLIST_DESC)
spotify.add_playlist_tracks(playlist, songs)





