import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow



SCOPES = ['https://www.googleapis.com/auth/youtube.readonly'] #the scope of the request, what we're asking to access. The reason this is a list is because we can ask for multiple scopes.

API_SERVICE_NAME = 'youtube'                       #name of the api we are trying to use
API_VERSION = 'v3'                                          #version of said api
CLIENT_SECRETS_FILE = "client_secret_605727893333-22mdqf7rskga469ts82k0ovmcf0a7rjg.apps.googleusercontent.com.json"             #The name of the client secrets file which contains all the info about our app such as client id, secret etc etc.


def get_service():      #define the function get_serivce()
    #flow = the class InstalledAppFlow on which the class method from_client_secrets_file() is called. (?)
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES) #the from_client_secrets_file() method has parameters for a client secrets json file and the scope, both of which are mentioned earlier. 
    
    #Run the OAuth process. User logs in, grants premissions to us, gives us authorization code (AC), we exchange AC for access token(AT) and refresh token(RT). AT allows us to make requests of API, RT gives new AT since AT is time limited. 
    credentials = flow.run_local_server(host="localhost", port = 2001)
    #credentials = flow.run_console()

    #Returns a service created using the build function
    return build("youtube", "v3", credentials = credentials)

service = get_service()


#define execute_api_request function.
def execute_api_request(client_library_function, **kwargs): #Parameters: (any function avaiable in the api library, Dont know what a kwarg is)
    
    #Use a function within a function
    response = client_library_function(**kwargs).execute()   #the execute method is needed to make the request of the API
    
    #print the response
    print(response)





if __name__ == '__main__':
      # Disable OAuthlib's HTTPs verification when running locally.
      # *DO NOT* leave this option enabled when running in production.
      os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
youtubedata = get_service()
execute_api_request(youtubedata.playlist().list(part="snippet,contentDetails", maxResults=25, mine=True))















# from ytmusicapi import YTMusic
# YTMusic.__init__

# from ytmusicapi import YTMusic
# ytmusic = YTMusic("oauth.json")

# playlistId = ytmusic.create_playlist("test", "test description")
# search_results = ytmusic.search("Oasis Wonderwall")
# ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])



# Create an instance of the YTMusic class
# ytmusic = YTMusic()

# # Call the get_playlist method with the playlistId and optional parameters
# playlist_id = "PLNJVokjI4uVhrA81c9wNlr6n2Ek8ntEYa"
# limit = None  # Adjust the limit as needed
# related = False
# suggestions_limit = 0

# # Get the playlist information
# gold_playlist = ytmusic.get_playlist(playlist_id, limit=limit, related=related, suggestions_limit=suggestions_limit)
#      #if you look in the get_playlistmethod you see that it return a dict contains a lot of info, first about the playlist as a whole and then about the individual tracks in the playlist
#      #under tracks you can therefore find a list of dicts. In each dict is stored info about an individual track

# # Print the playlist information
# for track in gold_playlist['tracks']:  #here gold_playlist['tracks'] refers to the subdict tracks, in which all the 
#     print(f"Track Name: {track['title']}") #f here refers to format. The expression within the curly braces {} is replaced with the value of ´track['title']´
#     print(f"Artist: {track['artists'][0]['name']}")
#     print("")

