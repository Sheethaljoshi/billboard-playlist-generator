import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date=input("Enter date to find Billboard's Hot 100 in YYYY-MM-DD: ")
special=input("Why is this day special? ")

URL = ("https://www.billboard.com/charts/hot-100/"+date)
response = requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")

songs_array=[song.getText().strip() for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="aac0f43c36f24154b7aa57d9e693c096",
        client_secret="d8268b639def4d83935e21f7252dc995",
        show_dialog=True,
        cache_path="token.txt",
        username="Sheethal", 
    )
)
user_id = sp.current_user()["id"]

song_uris=[]

year = date.split("-")[0]

for song_t in songs_array:
    name= sp.search(q=f"track:{song_t} year:{year}", type='track')
    try:
        uri=name["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song_t} doesn't exist in Spotify. Skipped.")
        
playlist = sp.user_playlist_create(user=user_id, name=f"{date} aKa - {special}", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)