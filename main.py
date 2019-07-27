""" 
* CREATED BY: CHRIS PUA, JULY 27, 2019
* Sample file to use BeautifulSoup and requests library, and to         import to CSV files.
* Just run main.py on terminal to see all functionality.
"""

# Web scraping library
from bs4 import BeautifulSoup
# Make use of the HTTP within Python in a more humanly readable way
import requests
import csv

url_link = "https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm"
page = requests.get(url_link)

soup = BeautifulSoup(page.text, 'html.parser')

# Removing unwanted links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

# Find div class containing list of artist names 
artist_name_list = soup.find(class_='BodyText')
# In the div class, find all <a> tags, which are links 
artist_name_list_items = artist_name_list.find_all('a')

f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    # Using getting to retrieve variable 'href' value
    links = 'https://web.archive.org/' + artist_name.get('href')
    
    # Add each artist's name and associated link to a row
    f.writerow([names,links])
    

