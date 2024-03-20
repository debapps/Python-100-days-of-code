import requests
from bs4 import BeautifulSoup

# This script scrapes the Empire Website to get the list of 100 top movies you should watch 
# and write them in the text file Top_100_Movies.txt.

OUT_FILE_NAME = './Top_100_Movies.txt'
EMPIRE_URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

# Get the content of the web page.
response = requests.get(url=EMPIRE_URL)
response.raise_for_status()
empire_web_content = response.text

# Create the soup with the web content.
movie_soup = BeautifulSoup(empire_web_content, 'html.parser')

# Get the list of top 100 movies.
top_100_movie_tag = movie_soup.select('.listicleItem_listicle-item__title__BfenH')
top_100_movie = [f'{movie.get_text()}\n' for movie in top_100_movie_tag]

# Write the top 100 movies into output text file.
with open(OUT_FILE_NAME, 'w+') as movie_file:
    movie_file.writelines(top_100_movie[::-1])