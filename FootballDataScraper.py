import re

import requests
from bs4 import BeautifulSoup
import pandas as pd

# WORK IN PROGRESS - Adding CSV functionality via pandas to extract stats to spreadsheet

# L2 Table Homepage - replace it with whatever League you wish that is available on that site.
url = "https://fbref.com/en/comps/16/League-Two-Stats"
page = requests.get(url)

soup = BeautifulSoup(page.text)

standings_table = soup.select('table.stats_table')[0]
links = standings_table.find_all('a')
links = [l.get("href") for l in links]
links = [l for l in links if '/squads/' in l]

teams = [f"https://fbref.com{l}" for l in links]


# Test for team stats ["number"] = index of teams position in the table (position -1). This example is Bradford City(14th)
team_url = teams[13]
data = requests.get(team_url)

fixtures = pd.read_html(data.text, match="Scores & Fixtures")

# Get specific stats for the team e.g. shooting
specifics = BeautifulSoup(data.text)
specLinks = specifics.find(href="#all_stats_shooting").get("href")
shootingURL = f"{team_url}+{specLinks}"


# Use the href's printed to choose your specific stat category. Replace href tag in the above
# example with your choice.
choice = specifics.find_all('a', href=re.compile("#all_"))

# iterate over results and print choices
for href in choice:
    print(href.get("href"))

print(shootingURL)









