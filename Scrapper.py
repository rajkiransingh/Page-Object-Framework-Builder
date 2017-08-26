# This file is to get all the top navigations from a retail website and create a page for all the categories
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

req = Request('https://www.mysite.com', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# HTML Parsing by SOUP
parsedHTML = soup(webpage,"html.parser")
print(parsedHTML.body.header)