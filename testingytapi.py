import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

#Create a flow class with the class method from_client_secrets_file. The method takes client info and scopes and contacts the google api to ask for credentials.
flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file= "webclientinfo.json", scopes = ['https://www.googleapis.com/auth/youtube.readonly'])

#Runs a local server which the user is redirected to.
flow.run_local_server(port=2001, prompt="consent", authorization_prompt_message="u just got scammed lol")

#The returned credentials using the flow class used above.
credentials = flow.credentials

#Print the returned credentials
print (credentials.to_json())

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

#For loop for printing the individual playlist titles
for playlist in playlist_list:
  #In reponse => items (list of playlists)
  #In items => snippets (dictionary of individual playlist)
  #In snippets => title (title of playlist key)
  playlist_title = playlist.get("snippet", {}).get("title")
  playlist_id = playlist.get("id")
  if playlist_title == "Walk thru wall":
    itemId = playlist_id; 
    print(f"Title: {playlist_title} \nID: {playlist_id}")


request2 = service.playlistItems().list(
  part="snippet",
  playlistId = itemId
  )

response2 = request2.execute()

playlist_songs = response2.get("items",[])
  
for song in playlist_songs:
  song_title = song.get("snippet", {}).get("title")
  print(song_title)