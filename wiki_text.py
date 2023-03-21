import requests
from bs4 import BeautifulSoup
import wiki_search

def user_page_selection():
    user_page_of_interest = input('Enter a page of interest: ')

    if user_page_of_interest in wiki_search.page_titles:
        print('Page found')
        index = wiki_search.page_titles.index(user_page_of_interest)
        return wiki_search.page_links[index]
    else:
        print('Enter a new value')
        user_page_selection()


url = user_page_selection()

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

text_list = []

for tag in soup.find_all('p'):
    text_list.append(tag.text)

print(' '.join(text_list))