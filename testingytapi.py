import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

credentials = None

# Pickle files are files that store python objects as bytestreams (basically just bytes)
# token.pickle stores the user's credentials from previously successful logins
if os.path.exists('token.pickle'): #if there exists a token.pickle file
    print('Loading Credentials From File...') 
    with open('token.pickle', 'rb') as token: #open the the token.pickle file and reads the bytestream (rb = read bytes) meaning that the token variable is assigned to a stream of the type bytes
        credentials = pickle.load(token)  #The pickle.load() function deserializes the bytestream contained in token(converts to a python object)

# If there are no valid credentials available, then either refresh the token or log in.
if not credentials or not credentials.valid: #If the credentials varible isn't assigned to anything or the credentials aren't valid:
    if credentials and credentials.expired and credentials.refresh_token: #if there are credentials and they've expired and there is a refresh token
        print('Refreshing Access Token...')
        credentials.refresh(Request()) #request a new access token from the google api using the refresh(request()) method
    else: #go through the oauth 2.0 to get access tokens and refresh tokens.
        print('Fetching New Tokens...')
        flow = InstalledAppFlow.from_client_secrets_file(
            "webclientinfo.json",
            scopes=[
                'https://www.googleapis.com/auth/youtube.readonly'
            ]
        )

        flow.run_local_server(port=2001, prompt='consent', authorization_prompt_message='u just got scammed lol')
        credentials = flow.credentials

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as f: #opens token.pickle in write byte mode
            print('Saving Credentials for Future Use...')
            pickle.dump(credentials, f) #serializes the credentials (turns credentials object into a bytestream) and stores it in the token.pickle file


# #Create a flow class with the class method from_client_secrets_file. The method takes client info and scopes and contacts the google api to ask for credentials.
# flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file= "webclientinfo.json", scopes = ['https://www.googleapis.com/auth/youtube.readonly'])

# #Runs a local server which the user is redirected to.
# flow.run_local_server(port=2001, prompt="consent", authorization_prompt_message="u just got scammed lol")

# #The returned credentials using the flow class used above.
# credentials = flow.credentials

# #Print the returned credentials
# print (credentials.to_json())

#Build a service object that is needed to make requests of google API
service = build("youtube", "v3", credentials = credentials)

#Requesting specifc information from google using their playlist() and list() methods.
request = service.playlists().list(
  part="snippet,contentDetails", #This "part" parameter limits the information requested to only what you ask for, reducing service load etc etc.
  maxResults=100,
  mine=True #this channel is mine
)

#Execute function is required to send the request to the google api. What is returned is a json dictionary, which response mirrors meaning response is a dictionary.
response = request.execute()

#Since reponse is a dictionary we can use the get() function to get all the values (in the form of a list) corresponding to the key "items". These values will themselves be dictionaries containing info about individual playlists for the account.
playlist_list = response.get("items", [])

itemID = []
item_name = []

#For loop for printing the individual playlist titles
for playlist in playlist_list:
  #In reponse => items (list of playlists)
  #In items => snippets (dictionary of individual playlist)
  #In snippets => title (title of playlist key)
  playlist_title = playlist.get("snippet", {}).get("title")
  playlist_id = playlist.get("id")
  # print(f"Title: {playlist_title}")
  #saved_pl = ["Summer", "Plugg spellista", "UK Bangerz", "Vibe mf", "Life", "Walk thru wall", "Wesley the 🐐", "Movie", "Oh mah gawd", "Forgotten bangerz", "25 låtar", "Slow times", "G(old)", "Workout", "Bangers"]
  saved_pl = ["Slow times"]
  if playlist_title in saved_pl:
    itemID.append(playlist_id)
    item_name.append(playlist_title)
    print(f"Title: {playlist_title} \nID: {playlist_id}")


print("")

#list of dict_lists
dict_list_list = []


for i in range(0, len(itemID)):
  print(f"\n \n")
  request2 = service.playlistItems().list(
    part="snippet",
    playlistId = itemID[i],
    maxResults = 50
    )

  response2 = request2.execute()

  #from reponse2, the "items" is a list that contains several hashmaps. An empty list is given as an argument in case there are no items in the list
  playlist_songs = response2.get("items",[])

  #list of track dictionaries
  dict_list = []

  print(f"Playlist: {item_name[i]} \n")
  for song in playlist_songs:
    song_title = song.get("snippet", {}).get("title")
    song_artist = song.get("snippet").get("videoOwnerChannelTitle")
    parsed_song_artist = song_artist.replace(" - Topic", "")
    song_dict = {song_title: parsed_song_artist}
    dict_list.append(song_dict)
    search_string = f"{song_title} {parsed_song_artist}"
    print(f"Song: {song_title}  &  Artist: {parsed_song_artist}")
    print(search_string)

dict_list_list.append(dict_list)

def some_function():
   return "Hi ya'll"

powerful_statement = True