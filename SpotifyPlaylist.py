import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from testingytapi import dict_list_list
from testingytapi import item_name


#Scope and OAuth authentication for search request
scope0 = "user-read-private"
sp0 = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope0))

#Search request:
query = []
track_list = []
for dict in dict_list_list:
    for track in dict:
        track_list.append(track)
        for key, value in track.items():
            query.append(f"{key} {value}")


index = 0               #index for getters.        
pl_url_list = []        #empty list. To contain track urls

found_tracks = []
missed_tracks = []

#Song and artist get functions
def get_song(index, list):
    for key, value in list[index].items():
        return key

def get_artist(index, list):
    for key, value in list[index].items():
        return value



#search for each song in query
for prompt in query:
    #result of search request
    results0 = sp0.search(q=prompt, type="track")

    #Variables used in results for loop
    has_track = False                    #variable to ensure only one track is added per search 
    item_results = results0.get("tracks").get("items")          #The track results from the search

    #For loop for adding track uris to the pl_track_list 
    for x in results0.get("tracks"):
        if x == "items":
            for idx, item in enumerate(item_results):
                track_name = item['name']
                artist_array = item["artists"] #the artist key is itself an array with one element, within which is a hashmap
                artist_name = artist_array[0].get("name") #here we go to the only element (index =0) and get the value for the key "name"
                track_uri = item["uri"]

                if track_name == get_song(index, track_list) and artist_name == get_artist(index, track_list) and has_track == False: #obviously the strings "COLD SUMMER" & "Wesley Joseph" are going to be changed to varibles representing the song names and artist names given by the yt music api
                    pl_url_list.append(track_uri)
                    found_tracks.append(track_list[index])
                    has_track = True

    index += 1


#Request for getting users ID 
results1 = sp0.me()
user_ID = results1.get("id")

#Scope and OAuth authentication for creating new playlist request
scope1 = "playlist-modify-private"
sp1 = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope1))

#Create a playlist and get its id.
results3 = sp1.user_playlist_create(user=user_ID, name=item_name[0], public= False)
new_pl_ID  = results3.get("id")

#populate new playlist with tracks
results5 = sp1.user_playlist_add_tracks(user=user_ID, playlist_id = new_pl_ID, tracks = pl_url_list, position=None)

#append all tracks that weren't found to the missed_tracks list
for track in track_list:
    if track not in found_tracks:
        missed_tracks.append(track)

#print missed tracks
print("All missed tracks: \n")
for idx in range(len(missed_tracks)):
    print (f"Track: {get_song(idx, missed_tracks)}, by: {get_artist(idx, missed_tracks)}")




