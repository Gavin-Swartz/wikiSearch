import difflib

import requests
from bs4 import BeautifulSoup
import wiki_search


def user_page_search(page_titles):

    user_search = input('Enter a topic you are interested in: ').lower()

    index = 0
    while index < len(page_titles):
        page_titles[index] = str(page_titles[index])
        index += 1

    return search(page_titles, user_search)


def search(page_titles, user_search):
    # Top 3 matches
    closest_matches = difflib.get_close_matches(user_search, page_titles)
    if len(closest_matches) > 0:
        index = 0
        while index < len(closest_matches):
            display_number = index + 1
            print(str(display_number) + '. ' + closest_matches[index])
            index += 1
        option = input('Which option best matches your search?')
        if option == str(1):
            index = page_titles.index(closest_matches[0])
            return wiki_search.page_links[index]
        elif option == str(2):
            index = page_titles.index(closest_matches[1])
            return wiki_search.page_links[index]
        elif option == str(3):
            index = page_titles.index(closest_matches[2])
            return wiki_search.page_links[index]
        else:
            print('Please enter a valid integer')
            search(page_titles, user_search)
    else:
        print('No valid results')
        user_page_search(page_titles)


url = user_page_search(wiki_search.page_titles)

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

text_list = []

for tag in soup.find_all('p'):
    text_list.append(tag.text)

print(' '.join(text_list))
