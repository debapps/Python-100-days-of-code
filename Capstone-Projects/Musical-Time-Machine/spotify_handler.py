from dotenv import load_dotenv
import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# This program uses spotify API to create a playlist of the song list provided.

# Load Environment file.
load_dotenv()

# Constants.
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URL = os.getenv('SPITIFY_REDIRECT_URL')
SCOPES = 'playlist-modify-private'

class SpotifyHandler:

    def __init__(self) -> None:
        # Create the spotify object.
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                                 client_secret=CLIENT_SECRET,
                                                                 redirect_uri=REDIRECT_URL,
                                                                 scope=SCOPES))
        # Get the current user id.
        user_data = self.spotify.me()
        self.user_id = user_data['id']

    def get_spotify_tracks(self, songs):
        tracks = []
        for song in songs:
            track_data = self.spotify.search(q=song, limit=1, offset=0, type='track', market='US')
            track_uri = track_data['tracks']['items'][0]['uri']
            tracks.append(track_uri)

        return tracks
    
    def create_playlist(self, name, desc=None):
        playlist_data = self.spotify.user_playlist_create(user=self.user_id, 
                                                 name=name, 
                                                 description=desc,
                                                 public=False, 
                                                 collaborative=False)
        
        playlist_id = playlist_data['id']
        print(f'\nPlaylist created successfully.\n\tID - {playlist_id}\n\tName - {name}')
        return playlist_id

    def add_playlist_tracks(self, playlist_id, songs):
        tracks = self.get_spotify_tracks(songs)

        data = self.spotify.playlist_add_items(playlist_id, tracks, position=None)
        print('\nAll songs are added successfully.')

        


# s = SpotifyHandler()
# playlist = s.create_playlist(name='My Test Playlist')
# s.add_playlist_tracks(playlist, ['This is What You Came For', 'Boba Tunnel'])