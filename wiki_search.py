import requests
from bs4 import BeautifulSoup


def find_site_links(soup):
    container = soup.find('div', {'id': 'mw-content-text'})
    links = container.find_all('a')
    return links


def get_page_title(link, page_titles, page_links):
    new_title = link.get('title')
    if new_title not in page_titles and not str(new_title).endswith('(page does not exist)') and not str(new_title).startswith('Special:BookSources/'):
        new_link = link.get('href')
        new_link = 'https://en.wikipedia.org' + new_link
        page_links.append(new_link)
        page_titles.append(new_title)


page_titles = []
page_links = []

# Computer article on Wikipedia
url = 'https://en.wikipedia.org/wiki/computers'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

links = find_site_links(soup)

for link in links:
    get_page_title(link, page_titles, page_links)

for title in page_titles:
    print(title)
