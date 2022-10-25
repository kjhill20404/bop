import spotipy
from spotipy.oauth2 import SpotifyOAuth,  SpotifyClientCredentials
import json
import requests

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="e594c3fd2d1d462ebdb519fc1ee41f95",
                                               client_secret="aba0078d73174856985b07b1f6eed18b",
                                               redirect_uri="http://localhost:8080",
                                               scope="user-library-read, playlist-read-private,user-read-playback-state,user-modify-playback-state"))

results = sp.current_user_playlists(50,0)
for i, item in enumerate(results['items']):
    #print("%d %s" % f{(i, item['name']) + str((item['id'])))
    print(f"{i} {(item['name'])} {(item['id'])}") 

play = input('what would you like to play? ')

#print(sp.devices())
#spotify:playlist:4T8nduGUdvQXgj0EKBZ6am
#results = sp.current_user_playlists(50,0)
song = 0
for i, item in enumerate(results['items']):
    #print(str(song))
    #print(sp.devices())
    if song == int(play):
        payload = {
            "device_id":"3324eed785b45487e72294010cb9c83a02a5cd11",
            "context_uri":f"{(item['uri'])}",
            "uris":"None",
            "offset":{
                "position":1
            }
        }
        #sp.start_playback(requests.post("https://api.spotify.com/v1/me/player/play", data=json.dumps(payload), headers={"Content-Type": "application/json"}))
        help = "['"+str(item['uri'])+"']"
        print(help)
        #device_id='3324eed785b45487e72294010cb9c83a02a5cd11'
        sp.start_playback(uris=help)
        print(f"{(item['uri'])} {(item['name'])}")
        break
    else:
        song = song + 1
        print(song)




