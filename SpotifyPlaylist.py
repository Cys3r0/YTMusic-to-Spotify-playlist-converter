import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from testingytapi import song_dict


#Scope and OAuth authentication for search request
scope0 = "user-read-private"
sp0 = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope0))

#Search request:
query = []
for dict in song_dict:
    query_item = f"{dict.item()} {dict.item().get()}"

#result of search request
results0 = sp0.search(q="cold summer wesley joseph", type="track")

#Variables used in results for loop
pl_track_list = []                 #empty list. To contain track urls
nr_o_tracks = 0                    #variable to ensure only one track is added per search 
item_results = results0.get("tracks").get("items")          #The track results from the search

#For loop for adding track uris to the pl_track_list 
for x in results0.get("tracks"):
    if x == "items":
        for idx, item in enumerate(item_results):
            track_name = item['name']
            artist_array = item["artists"] #the artist key is itself an array with one element, within which is a hashmap
            artist_name = artist_array[0].get("name") #here we go to the only element (index =0) and get the value for the key "name"
            track_uri = item["uri"]
            if track_name == "COLD SUMMER" and artist_name == "Wesley Joseph" and nr_o_tracks < 1: #obviously the strings "COLD SUMMER" & "Wesley Joseph" are going to be changed to varibles representing the song names and artist names given by the yt music api
                pl_track_list.append(track_uri)
                nr_o_tracks+=1
            print(f"{idx}, {track_name}, {artist_name}, {track_ID}")

#Request for getting users ID 
results1 = sp0.me()
user_ID = results1.get("id")
print(f"{user_ID}")

#Scope and OAuth authentication for creating new playlist request
scope1 = "playlist-modify-private"
sp1 = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope1))

#Create a playlist and get its id.
results3 = sp1.user_playlist_create(user=user_ID, name="test", public= False)
new_pl_ID  = results3.get("id")
print(new_pl_ID)

#populate new playlist with tracks
results5 = sp1.user_playlist_add_tracks(user=user_ID, playlist_id = new_pl_ID, tracks = pl_track_list, position=None)






# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])


# SPOTIPY_CLIENT_ID = "0a65f57e85c74a42bdc0dbacbe124f31"
# SPOTIPY_CLIENT_SECRET = "25cd7b21a49e4abdb510a3dd8534b1dc"
# SPOTIPY_REDIRECT_URI = "https://localhost:1960/callback"


# #Find playlist ID to populate newly created playlist.
# results4 = sp0.user_playlists(user = user_ID, limit=100)
# user_playlists = results4.get("items")
# for playlist in user_playlists:
#     print(playlist.get("name"))
#     # if playlist[0].get("name") == "test": #replace "test" with varible for playlist name
#     #     playlist_ID = playlist[0].get("id")
#     #     print("Huh")

# # #Define the scope of the access this application is asking for. To create a new playlist our scope is: "playlist-modify-private"
# scope = "playlist-modify-private"

# # #Create instance of SpotifyOAuth class, which needs a scope as an arguement. 
# # #The SpotifyAOuth class handles OAuthenication 2.0 with the Spotify Web Api. It provides the environmental variables SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET and SPOTIPY_REDIRECT_URI to request access to the Spotify api.
# # #Sends the user to log in on their spotidfy account.
# # #Also makes the request of the Spotify Web Api for an Authorization code, which later can be exchanged for an Access Token.
# # #The Access Token allows the application to make requests of the Spotify Web Api on behalf of the user without giving away the users credentials.
# # #Also refreshes Access Tokens as they tend to be limited time only.  
# auth_manager = SpotifyOAuth(scope=scope)

# # #Create an instance of the Spotify class, using the SpotifyOAuth class as a param. The Spotify class is used to communicate with the spotify web API  
# sp = spotipy.Spotify(auth_manager)

# # #Use the user_playlist_create() method found in the spotipy api in order to create a playlist for our 
# search_tracks = sp.search(q="track: cold summer", type="track")
# print(search_tracks)




#Heres the plan. Use the search() method which returns an Array of Tracks object which should be able to be used.
#Using this Array of tracks object there I should be able to match the title of the song and the artist to the corresponding provided through the google api. If A track can't be found to match perfectly, It should take the first one or add none.