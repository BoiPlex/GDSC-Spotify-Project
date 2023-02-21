import spotipy
from spotipy.oauth2 import SpotifyOAuth


#user auth
CLIENT_ID = "162776f8116f492ca95030ddf7370e2a"
CLIENT_SECRET = "9c2e49219ec2427cb67f3884898f6f7f"
REDIRECT_URI = "http://127.0.0.1:8080/"

USERNAME = input("Input spotify username: ")

#getting data
SCOPE = 'user-top-read'

token = SpotifyOAuth(scope=SCOPE, username=USERNAME, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
GetTopListen = spotipy.Spotify(auth_manager=token)

result = GetTopListen.current_user_top_artists(time_range = "long_term")
topArtists = {}
for i, item in enumerate(result['items']):
    topArtists[i] = item

result = GetTopListen.current_user_top_tracks(time_range = "long_term")
topTracks = {}
for i, item in enumerate(result["items"]):
    topTracks[item['name']] = item['artists'][0]['name']