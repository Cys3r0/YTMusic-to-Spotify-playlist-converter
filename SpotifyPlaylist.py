import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])



scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

    


# #Define the scope of the access this application is asking for. To create a new playlist our scope is: "playlist-modify-private"
# scope = "playlist-modify-private"

# #Create instance of SpotifyOAuth class, which needs a scope as an arguement. 
# #The SpotifyAOuth class handles OAuthenication 2.0 with the Spotify Web Api. It provides the environmental variables SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET and SPOTIPY_REDIRECT_URI to request access to the Spotify api.
# #Sends the user to log in on their spotidfy account.
# #Also makes the request of the Spotify Web Api for an Authorization code, which later can be exchanged for an Access Token.
# #The Access Token allows the application to make requests of the Spotify Web Api on behalf of the user without giving away the users credentials.
# #Also refreshes Access Tokens as they tend to be limited time only.  
# auth_manager = SpotifyOAuth(scope=scope)

# #Create an instance of the Spotify class, using the SpotifyOAuth class as a param. The Spotify class is used to communicate with the spotify web API  
# sp = spotipy.Spotify(auth_manager)

# #Use the user_playlist_create() method found in the spotipy api in order to create a playlist for our 
# newplaylist = sp.user_playlist_create()








