import requests
from bs4 import BeautifulSoup

# Computer article on Wikipedia
url = 'https://en.wikipedia.org/wiki/Computer'

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

text_list = []

for tag in soup.find_all('p'):
    text_list.append(tag.text)

print(' '.join(text_list))