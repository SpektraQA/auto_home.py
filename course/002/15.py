import requests
import re
# from requests.exceptions import HTTPError
# url = 'https://xkcd.com/353/'
#
# response = requests.get(url, timeout=10)
#
# # print(response.headers['SerVer'])
#
# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occured: {http_err}')
#     else:
#         print('Success')

from bs4 import BeautifulSoup as BS

url = 'https://www.gammatest.net/course/python'

response = requests.get(url)

soup = BS(response.content, 'html.parser')

# print(soup.div['class'])
# print(soup.a['href'])

# match = soup.find('div', class_='col-md-8')
# print(match.h2.text)

# matches = soup.find_all(type='text/javascript')
# print(soup.div.get_attribute_list)

# print(soup.find_all(string=False))

matches = soup.td.()
print(matches)