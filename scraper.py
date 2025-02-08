import requests
from bs4 import BeautifulSoup

def get_trending_topics():
    url = "https://www.linkedin.com/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    topics = [item.text for item in soup.find_all("h3", class_="feed-shared-article__title")][:5]
    return topics
