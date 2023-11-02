from ytmusicapi import YTMusic

YTMusic.__init__

# Create an instance of the YTMusic class
ytmusic = YTMusic()

# Call the get_playlist method with the playlistId and optional parameters
playlist_id = "PLNJVokjI4uVhrA81c9wNlr6n2Ek8ntEYa"
limit = None  # Adjust the limit as needed
related = False
suggestions_limit = 0

# Get the playlist information
gold_playlist = ytmusic.get_playlist(playlist_id, limit=limit, related=related, suggestions_limit=suggestions_limit)
     #if you look in the get_playlistmethod you see that it return a dict contains a lot of info, first about the playlist as a whole and then about the individual tracks in the playlist
     #under tracks you can therefore find a list of dicts. In each dict is stored info about an individual track

# Print the playlist information
for track in gold_playlist['tracks']:  #here gold_playlist['tracks'] refers to the subdict tracks, in which all the 
    print(f"Track Name: {track['title']}") #f here refers to format. The expression within the curly braces {} is replaced with the value of ´track['title']´
    print(f"Artist: {track['artists'][0]['name']}")
    print("")


# Jesus christ what am i doing in this part??
# for i in goldplaylist:
#     value = goldplaylist[i]
#     if isinstance(value, list):
#         strlist = list(map(str, value))
#         print(i + " = ".join(strlist))
#     elif value is None:
#         print(i + " = " + "None")
#     elif isinstance(dict, value):
#         for q in value:
#             realvalue = value[q]
#     else:
#         print(i + " = " + value)
#    curl -X POST "https://accounts.spotify.com/api/token" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id=0a65f57e85c74a42bdc0dbacbe124f31&client_secret=25cd7b21a49e4abdb510a3dd8534b1dc"


#    curl "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb" -H "Authorization: Bearer  BQBANT601rej_BGE9BrBZ7lSKFzYei2XWz_U12MM-wZOnz87-1DlSXKgQ8P6ltQKy9b5QK9R3yXv945AgH1VbWD7ys719f6Oq58FNSoKRiCsMLT2Q3I"

# """
# curl --request POST --url https://api.spotify.com/v1/users/smedjan/playlists --header 'Authorization: Bearer BQBANT601rej_BGE9BrBZ7lSKFzYei2XWz_U12MM-wZOnz87-1DlSXKgQ8P6ltQKy9b5QK9R3yXv945AgH1VbWD7ys719f6Oq58FNSoKRiCsMLT2Q3I' --header 'Content-Type: application/json' --data '{"name": "New Playlist","description": "New playlist description","public": false}
# """