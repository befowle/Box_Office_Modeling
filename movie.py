#import required packages
import requests
from bs4 import BeautifulSoup as BS

#scrape webpage
url="https://www.boxofficemojo.com/year/2018/?grossesOption=totalGrosses&sortDir=asc&sort=releaseDate&ref_=bo_yld__resort#table"

#let's use the function we already created
page = requests.get(url)

soup = BS(page.content, 'html.parser')

#show full html
long_thing=print(soup.prettify())

#find movie names in html
titles=soup.find('td', class_='a-text-left mojo-field-type-release mojo-cell-wide')
names=soup.find_all('td', class_='a-text-left mojo-field-type-release mojo-cell-wide')

#create list of movie names
All_names = []
for thing in names:
    try:
        All_names.append(thing.string)
    except:
        All_names.append('NAN')
        continue

#split revenue into 2 lists: one for gross revenue, one for opening weekend
gross_opening=soup.find_all('td', class_='a-text-right mojo-field-type-money')

i=0
gross=[]
opening=[]
for thing in gross_opening:
    if i%2==0:
        gross.append(gross_opening[i].string)
    elif i%2!=0:
        opening.append(gross_opening[i].string)
    i+=1

# create list of opening dates
opening_date=soup.find_all('td', class_='a-text-left mojo-field-type-date mojo-sort-column a-nowrap')

All_opening_dates = []
for thing in opening_date:
    try:
        All_opening_dates.append(thing.string)
    except:
        All_opening_dates.append('NAN')
        continue
