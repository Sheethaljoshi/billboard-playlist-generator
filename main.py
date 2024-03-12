import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date=input("Enter date to find Billboard's Hot 100 in YYYY-MM-DD: ")

URL = ("https://www.billboard.com/charts/hot-100/"+date)
response = requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")

songs_array=[song.getText().strip() for song in songs]

for song_t in songs_array:
    print(song_t)

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