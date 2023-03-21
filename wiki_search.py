import requests
from bs4 import BeautifulSoup


def find_site_links(soup):
    container = soup.find('div', {'id': 'mw-content-text'})
    links = container.find_all('a')
    return links


def get_page_title(link, page_titles, page_links):
    new_title = link.get('title')
    if new_title not in page_titles and not str(new_title).endswith('(page does not exist)'):
        new_link = link.get('href')
        new_link = 'https://en.wikipedia.org' + new_link
        page_links.append(new_link)
        page_titles.append(new_title)


def user_page_selection():
    user_page_of_interest = input('Enter a page of interest: ')

    if user_page_of_interest in page_titles:
        print('Page found')
        index = page_titles.index(user_page_of_interest)
        print(page_links[index])
    else:
        print('Enter a new value')
        user_page_selection()


page_titles = []
page_links = []

# Computer article on Wikipedia
url = 'https://en.wikipedia.org/wiki/Computer'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

links = find_site_links(soup)

for link in links:
    get_page_title(link, page_titles, page_links)

for title in page_titles:
    print(title)

print(len(page_links))
print(len(page_titles))

user_page_selection()
