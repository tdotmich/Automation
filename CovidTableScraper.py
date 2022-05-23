import requests
from bs4 import BeautifulSoup
import pandas as pd
#  A script that will grab current Covid info an extract to a csv file.

# URL object - the page we want to scrape from
url = 'https://www.worldometers.info/coronavirus/'

# Object page. "<200>" response means server approves request
page = requests.get(url)

# parser-lxml = HTML to Python format

# obtain page info
soup = BeautifulSoup(page.text, 'lxml')
soup

# Grab info from page. Table tag <table>
covidTab = soup.find('table', id='main_table_countries_today')
covidTab

# Headers begin with <th> - extract these
headers = []
for i in covidTab.find_all('th'):
    title = i.text
    headers.append(title)

# Convert wrapped text in column 13 into one line text
headers[13] = 'Tests/1M pop'

# Create dataframe to store table in
tabData = pd.DataFrame(columns=headers)

# For loop to fill table
for j in covidTab.find_all('tr')[1:] :
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(tabData)
    tabData.loc[length] = row

# Drop the rows we don't need - these are at the top and bottom of the tabdata
tabData.drop(tabData.index[0:7], inplace=True)
tabData.drop(tabData.index[236:249], inplace=True)
tabData.reset_index(inplace=True, drop=True)


# send dataframe to a csv for reading in env file path
tabData.to_csv("coviddata.csv", index=False)
dataRead = pd.read_csv("coviddata.csv")









