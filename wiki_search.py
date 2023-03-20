import requests
from bs4 import BeautifulSoup


def find_site_links(soup):
    container = soup.find('div', {'id': 'mw-content-text'})
    links = container.find_all('a')
    return links


def get_link_urls(links, links_list):
    for link in links:
        new_link = link.get('href')
        new_link = str(new_link)
        if new_link.startswith('/wiki/') and new_link not in links_list:
            new_link = 'https://en.wikipedia.org/' + new_link
            links_list.append(new_link)
    return links_list



links_list = []

# Computer article on Wikipedia
url = 'https://en.wikipedia.org/wiki/Computer'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

links = find_site_links(soup)

site_urls = get_link_urls(links, links_list)
print(site_urls)

