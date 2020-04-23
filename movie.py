#import required packages
import requests
from bs4 import BeautifulSoup as BS
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.parser import parse

#scrape Box Office Mojo webpage
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

#create array of gross revenue to clean data
gross_array=np.array(gross)

gross_numbers=[]
for item in gross:
    maybe = item.strip('$')
    maybe2=maybe.strip(',')
    maybe3 = maybe2.replace(',','')
    maybe4=int(maybe3)
    gross_numbers.append(maybe4)

#repeat for opening numbers
opening_numbers=[]
for item in opening:
    try:
        maybe = item.strip('$')
        maybe2=maybe.strip(',')
        maybe3 = maybe2.replace(',','')
        maybe4=int(maybe3)
        opening_numbers.append(maybe4)
    except:
        opening_numbers.append(item)

#zip, tuple, and list clean numbers
zipped_opening_gross=zip(opening_numbers,gross_numbers)
zipped_opening_gross_tuple=list(zipped_opening_gross)
zipped_opening_gross_clean = list(filter(lambda x: '-' not in x, zipped_opening_gross_tuple))

#split into separate lists
opening_clean= [x[0] for x in zipped_opening_gross_clean]
gross_clean = [x[1] for x in zipped_opening_gross_clean]

# create list of opening dates
opening_date=soup.find_all('td', class_='a-text-left mojo-field-type-date mojo-sort-column a-nowrap')

All_opening_dates = []
for thing in opening_date:
    try:
        All_opening_dates.append(thing.string)
    except:
        All_opening_dates.append('NAN')
        continue

# create list of closing dates
closing_date=soup.find_all('td', class_='a-text-left mojo-field-type-date a-nowrap')
All_closing_dates = []
for thing in closing_date:
    try:
        All_closing_dates.append(thing.string)
    except:
        All_closing_dates.append('NAN')
        continue

#clean date lists
release_date_clean=[]
for thing in All_opening_dates:
    y=thing.replace('Jan ','2018-01-')
    y2=y.replace('Feb ','2018-02-')
    y3=y2.replace('Mar ','2018-03-')
    y4=y3.replace('Apr ','2018-04-')
    y5=y4.replace('May ','2018-05-')
    y6=y5.replace('Jun ','2018-06-')
    y7=y6.replace('Jul ','2018-07-')
    y8=y7.replace('Aug ','2018-08-')
    y9=y8.replace('Sep ','2018-09-')
    y10=y9.replace('Oct ','2018-10-')
    y11=y10.replace('Nov ','2018-11-')
    y12=y11.replace('Dec ','2018-12-')
    release_date_clean.append(y12)

closing_date_clean=[]
for thing in All_closing_dates:
    y=thing.replace('Jan ','2018-01-')
    y2=y.replace('Feb ','2018-02-')
    y3=y2.replace('Mar ','2018-03-')
    y4=y3.replace('Apr ','2018-04-')
    y5=y4.replace('May ','2018-05-')
    y6=y5.replace('Jun ','2018-06-')
    y7=y6.replace('Jul ','2018-07-')
    y8=y7.replace('Aug ','2018-08-')
    y9=y8.replace('Sep ','2018-09-')
    y10=y9.replace('Oct ','2018-10-')
    y11=y10.replace('Nov ','2018-11-')
    y12=y11.replace('Dec ','2018-12-')
    closing_date_clean.append(y12)

#calculate time in theater
release_date_date_time=[]
for thing in release_date_clean:
        y2=datetime.strptime(thing,'%Y-%m-%d')
        release_date_date_time.append(y2)

closing_date_date_time=[]
for thing in closing_date_clean:
    print(thing)
    try:
        y2=datetime.strptime(thing,'%Y-%m-%d')
        closing_date_date_time.append(y2)
    except:
        closing_date_date_time.append(thing)

i=0
subtracted_o_c=[]
for thing in range(len(closing_date_date_time)):
    try:
        subtracted=closing_date_date_time[i]-release_date_date_time[i]
        subtracted_o_c.append(subtracted)
        i+=1
    except:
        subtracted_o_c.append('-')
        i+=1

days_in_theatre=[]
for thing in subtracted_o_c:
    try:
        print(thing)
        days_in_theatre.append(int(str(thing).split()[0]))
        print(days_in_theatre)
    except:
        days_in_theatre.append('-')

days_in_theatre_with_none=[]
for item in days_in_theatre:
    if type(item)==int:
        days_in_theatre_with_none.append(item)
    else:
        days_in_theatre_with_none.append(None)
        continue

opening_numbers_with_none=[]
for item in opening_numbers:
    if type(item)==int:
        opening_numbers_with_none.append(item)
    else:
        opening_numbers_with_none.append(None)
        continue

gross_numbers_with_none=[]
for item in gross_numbers:
    if type(item)==int:
        gross_numbers_with_none.append(item)
    else:
        gross_numbers_with_none.append(None)
        continue

i=0
All_data_mojo=[]
for thing in range(len(All_names)):
    new_tuple = (All_names[i],days_in_theatre_with_none[i],opening_numbers_with_none[i],gross_numbers_with_none[i])
    All_data_mojo.append(new_tuple)
    i+=1

#additional cleaning
All_data_mojo_None_replaced_for_dash=list(All_data_mojo[7])[2].replace('-','NAN')

#save data frames
opening_numbers_pd=pd.DataFrame(opening_numbers)
opening_numbers_pd.to_csv('opening_numbers.csv')
gross_numbers_pd=pd.DataFrame(gross_numbers)
gross_numbers_pd.to_csv('gross_numbers.csv')
All_names_pd=pd.DataFrame(All_names)
All_names_pd.to_csv('All_names.csv')
closing_date_clean_pd=pd.DataFrame(closing_date_clean)
closing_date_clean_pd.to_csv('closing_date_clean.csv')
release_date_clean_pd=pd.DataFrame(release_date_clean)
release_date_clean_pd.to_csv('release_date_clean.csv')
days_in_theatre_pd=pd.DataFrame(days_in_theatre)
days_in_theatre_pd.to_csv('days_in_theatre.csv')
