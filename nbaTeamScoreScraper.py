"""
* CREATED BY: CHRIS PUA - JULY 27, 2019
* Main file containing scraper 
"""

from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Chris Pua, <url>',
    'From': 'chris.pua@mail.utoronto.ca'
}
# TODO: Switch URLS to this -> https://www.espn.com/nba-summer-league/scoreboard
# TODO: It would have all the games in one page to make life easier 
url = 'https://www.espn.com/nba/boxscore?gameId=401134820'
page = requests.get(url, headers = headers)
soup = BeautifulSoup(page.text, 'html.parser')

print ('\nFinal Score')

awayBoxScore = soup.find(class_ = 'col column-one gamepackage-away-wrap')
awayStats = awayBoxScore.find_all('tr', 'highlight')
awayName = awayBoxScore.find('div', class_= 'team-name').get_text()

awayPoints = -1

for item in awayStats:
    awayPoints = item.find('td', 'pts').string
    if awayPoints is not None:
        print(awayName + ': ' + awayPoints)
        break


homeBoxScore = soup.find(class_ = 'col column-two gamepackage-home-wrap')
homeStats = homeBoxScore.find_all('tr', 'highlight')
homeName = homeBoxScore.find('div', class_= 'team-name').get_text()

homePoints = -1

for item in homeStats:
    homePoints = item.find('td', 'pts').string
    if homePoints is not None:
        print(homeName  + ': ' + homePoints)
        break
    