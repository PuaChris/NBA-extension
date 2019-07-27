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

""" 
! CHECK THE WEBISTE FOR TERMS AND CONDITIONS, AND TO SEE IF THEY HAVE AN API THAT ALLOWS YOU TO GRAB DATA.
! IT'S ALSO A GOOD IDEA TO SCRAPE WITH A HEADER THAT HAS YOUR NAME AND EMAIL
""" 

headers = {
    'User-Agent': 'Chris Pua, web.archive.org',
    'From': 'chris.pua@mail.utoronto.ca'
}

f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

pages = []
# In the URL link, the number after the 'anZ' changes when you switch pages 
for i in range (1,5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)
    
for item in pages:
    page = requests.get(item, headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Removing unwanted links
    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    # Find div class containing list of artist names 
    artist_name_list = soup.find(class_='BodyText')
    # In the div class, find all <a> tags, which are links 
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        # Using getting to retrieve variable 'href' value
        links = 'https://web.archive.org/' + artist_name.get('href')
        
        # Add each artist's name and associated link to a row
        f.writerow([names,links])
        

    
