from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(r.text, "html.parser")

titles = ([title.getText() for title in soup.select("span h2 strong")])[::-1]

with open('top_100_movies.txt', 'a') as file :
	for title in titles :
		file.write(f"{title}\n")