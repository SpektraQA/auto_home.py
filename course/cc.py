import requests
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

usd_to_yen = 'https://www.google.com/search?q=usd+to+yen&sca_esv=580203348&sxsrf=AM9HkKnDY7sPouUaC1yIvAtonRVM8YNlFg%3A1699382714762&ei=uoVKZeSNLrvPxc8P7uSDgA8&ved=0ahUKEwjk0rP4xbKCAxW7Z_EDHW7yAPAQ4dUDCBA&uact=5&oq=usd+to+yen&gs_lp=Egxnd3Mtd2l6LXNlcnAiCnVzZCB0byB5ZW4yBxAjGIoFGCcyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgoQABiABBgUGIcCMgUQABiABEiNMVCTH1ilLnACeAGQAQGYAcoCoAH2BqoBBzAuNC4wLjG4AQPIAQD4AQHCAgoQABhHGNYEGLADwgIKEAAYigUYsAMYQ8ICBxAAGIoFGEPCAgsQABiABBixAxiDAcICDRAAGIAEGLEDGIMBGArCAgcQABiABBgK4gMEGAAgQYgGAZAGCg&sclient=gws-wiz-serp'
response = requests.get(usd_to_yen, headers=headers)

soup = BS(response.content, 'html.parser')

data = soup.find('span', class_='DFlfde SwHCTb')
print(data.text)


