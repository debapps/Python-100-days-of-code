from bs4 import BeautifulSoup
import requests

URL = 'https://news.ycombinator.com/'

# Get the constent of the webpage.
response = requests.get(url=URL)
response.raise_for_status()
y_combinator_news = response.text

# with open('content.html', 'w+') as out:
#     out.write(y_combinator_news)

# Create the soup out the webpage content.
soup = BeautifulSoup(y_combinator_news, 'html.parser')

# Get all the article text, article link and article score.
articles = soup.select('.titleline > a')
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)

    link = article_tag.get('href')
    article_links.append(link)

article_scores = [int(score.get_text().split(' ')[0]) 
                  for score in soup.select('.score')]


# Get the index of the max scores.
max_idx = article_scores.index(max(article_scores))


# Get the article text, link of the maximum score.
print(f'\nThe top rated article in the {soup.title.string}\n')
print(f'\tHeading: {article_texts[max_idx]}')
print(f'\tLink: {article_links[max_idx]}')
print(f'\tVotes: {article_scores[max_idx]}\n')


# for article in article_texts:  
#     print(article)

# for score in article_scores:
#     print(score)





