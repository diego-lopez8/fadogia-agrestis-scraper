"""
scraper.py
Author: Diego Lopez
Date: 08/10/2021
This file contains code that scrapes a webpage for a popular supplement called Fadogia Agrestis that is very hard to 
obtain these days. It runs once, however in main.py it is looped to scrape every 30 seconds
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import time

def scrape(url):
    try:
        html = urlopen(url)
    except HTTPError as error:
        print(error)
    except URLError as error:
        print("Incorrect domain or the server is down\n")
    else:
        soup         = BeautifulSoup(html.read(), 'html5lib')
        in_stock     = False
        availability = soup.find('meta', property = 'product:availability')
        if availability['content'] != "out of stock":
            in_stock = True
        return in_stock
