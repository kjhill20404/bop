import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="e594c3fd2d1d462ebdb519fc1ee41f95",
                                               client_secret="aba0078d73174856985b07b1f6eed18b",
                                               redirect_uri="http://localhost:8080",
                                               scope="user-library-read, playlist-read-private,user-read-playback-state,user-modify-playback-state"))

# Shows playing devices
res = sp.devices()
pprint(res)

# Change track
sp.start_playback(uris=['spotify:playlist:6RQrm05Qz2S2BwjIwwjqSz'])

# Change volume
sp.volume(100)
sleep(2)
sp.volume(50)
sleep(2)
sp.volume(100)


