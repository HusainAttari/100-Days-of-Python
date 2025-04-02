import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
USERNAME = os.getenv("USERNAME")
REDIRECT_URI = os.getenv("REDIRECT_URI")

date = input("What date would you like to travel to? [YYYY-MM-DD] : ")

billboard_header = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
	}

bb_url = f'https://www.billboard.com/charts/hot-100/{date}'
r = requests.get(bb_url, headers=billboard_header)
r.raise_for_status()
soup = BeautifulSoup(r.text, 'html.parser')

title_spans = soup.select("li ul li h3")
titles = [title.getText().strip() for title in title_spans]

artist_spans = soup.select("li ul li span")
artists = [artist.getText().strip() for artist in artist_spans]

sp = spotipy.Spotify(
	auth_manager=SpotifyOAuth(
		client_id=SPOTIFY_CLIENT_ID,
		client_secret=SPOTIFY_CLIENT_SECRET,
		redirect_uri=REDIRECT_URI,
		cache_path="token.txt",
		username=USERNAME,
		scope="playlist-modify-private",
		show_dialog=True
		)
	)

user_id = sp.current_user()['id']
print(user_id)

song_uris = []
for i in range(len(titles)) :
	result = sp.search(q=f"{titles[i]} {artists[i]}", type="track")
	try :
		uri = result["tracks"]["items"][0]["uri"]
		song_uris.append(uri)
	except IndexError :
		print(f"{titles[i]} doesn't exist on Spotify. Skipped.")

playlist_id = sp.user_playlist_create(user_id, name=f"{date} Billboard Top 100", public=False)['id']

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)