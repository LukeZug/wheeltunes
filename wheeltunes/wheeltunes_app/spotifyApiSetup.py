import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Setup API credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="4a6931abd97b4611b9deecb921964b58", client_secret="####"))

