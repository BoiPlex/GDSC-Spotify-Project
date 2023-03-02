import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask_login import login_required, current_user

#user auth
CLIENT_ID = "71adcded9d2e46ff98e58321ee78ac68"
CLIENT_SECRET = "c9d5d21401e84e5aa3d39cca19d593d2"
REDIRECT_URI = "http://localhost:8888/callback"
# "162776f8116f492ca95030ddf7370e2a"
# "9c2e49219ec2427cb67f3884898f6f7f"
# "http://127.0.0.1:5000/"

def getData(spotifyUsername):
    USERNAME = spotifyUsername

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

    return topArtists, topTracks

print(getData("Karim"))