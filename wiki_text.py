import requests
from bs4 import BeautifulSoup
import wiki_crawler


def print_titles(page_titles):
    print_index = 0
    for title in page_titles:
        print(str(print_index + 1) + '. ' + title)
        print_index += 1

    print(str(len(page_titles)) + ' results')


def user_page_search(page_links):
    user_search = input('Enter the number of the topic you are interested in: ')
    selected_url = page_links[int(user_search) - 1]
    return selected_url


def get_text(soup):
    text_list = []
    for tag in soup.find_all('p'):
        text_list.append(tag.text)
    print(' '.join(text_list))


print_titles(wiki_crawler.page_titles)
url = user_page_search(wiki_crawler.page_links)

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

get_text(soup)
