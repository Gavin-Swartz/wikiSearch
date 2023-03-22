import difflib
import requests
from bs4 import BeautifulSoup
import wiki_search


def user_page_search(page_links):
    user_search = input('Enter the number of the topic you are interested in: ')
    selected_url = page_links[int(user_search) -1]
    return selected_url


url = user_page_search(wiki_search.page_links)

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

text_list = []

for tag in soup.find_all('p'):
    text_list.append(tag.text)

print(' '.join(text_list))
