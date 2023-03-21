import requests
from bs4 import BeautifulSoup
import wiki_articles as articles


def find_site_links(soup):
    container = soup.find('div', {'id': 'mw-content-text'})
    links = container.find_all('a')
    return links


def get_page_title(link, page_titles, page_links):
    new_title = link.get('title')
    new_title = str(new_title).lower()
    if new_title not in page_titles and not new_title.endswith('(page does not exist)') and\
            not new_title.startswith('special:') and new_title != 'None':
        new_link = link.get('href')
        if new_link is not None:
            new_link = str(new_link)
            new_link = 'https://en.wikipedia.org' + new_link
            page_links.append(new_link)
            page_titles.append(new_title)


def choose_article():
    index = 0
    for article in articles.links:
        print(str(index + 1) + '. ' + article)
        index += 1
    user_choice = int(input('Choose an article to pull links from: '))
    url = articles.links[user_choice - 1]
    return url


page_titles = []
page_links = []

url = choose_article()

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

links = find_site_links(soup)

for link in links:
    get_page_title(link, page_titles, page_links)

for title in page_titles:
    print(title)
print(str(len(page_titles)) + ' results')
