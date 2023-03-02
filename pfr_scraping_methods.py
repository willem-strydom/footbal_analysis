import pandas as pd
import requests
import os
from dotenv import load_dotenv
import lxml
from bs4 import BeautifulSoup
import dataset_management_methods as dmm

#team_abbr here is whatever pro_football_reference uses in the html, not necessarily what the NFL uses as the abbrevation
#could be useful to write a function that can convert a team name to the abbreviation later on
def retrieve_team_data(team_abbr : str, year : int) -> pd.DataFrame():
    table_label = 'games'
    abbr = team_abbr.lower()
    url = f'https://www.pro-football-reference.com/teams/{abbr}/{year}.htm#{table_label}'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, features="lxml")
    headers = [th.getText() for th in soup.findAll('tr')[7].findAll('th')]
    headers = headers[1:]
    rows = soup.findAll('tr', class_ = lambda table_rows: table_rows != "thead")
    team_results = [[td.getText() for td in rows[i].findAll('td')] for i in range(8,26)]
    team_data = pd.DataFrame(team_results, columns=headers)
    return team_data

# seahawks = retrieve_team_data('sea', 2022)
# print(seahawks)

#alters name format to make string easier to parse for url
def fix_name(full_name : str):
    new_name = full_name.split()
    fixed_name = []
    for name in new_name:
        lowercase = name.lower()
        capitalized = lowercase.capitalize()
        fixed_name.append(capitalized)
    return fixed_name

def retrieve_player_data(player_full_name : str, year : int) -> pd.DataFrame():
    first_and_last = fix_name(player_full_name)
    unique_player_string = first_and_last[1][:4] + first_and_last[0][:2] + '00'
    url = f'https://www.pro-football-reference.com/players/{first_and_last[0]}/{unique_player_string}/gamelog/{year}/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, features="lxml")
    headers = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
    #print(headers)
    headers = headers[1:]
    rows = soup.findAll('tr', class_ = lambda table_rows: table_rows != "thead")
    player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(2,19)]
    player_data = pd.DataFrame(player_stats, columns=headers)
    #want to now reduce this dataframe down to the columns we need
    player_data = player_data[['Date','','Opp','Rate']]
    return player_data

def clean_and_normalize_dataset(df : pd.DataFrame) -> pd.DataFrame:
    distances = [dmm.calculate_distance('SEA', opponent) for opponent in df['Opp']]
    df['Miles Traveled'] = distances
    df.loc[9, 'Miles Traveled'] = dmm.calculate_distance('SEA', 'GER')
    #we had to manually assign this value because this is an edge case
    df = df.rename(columns={"":"Home/Away"})
    sites = []
    for site in df['Home/Away']:
        if site=='':
            sites.append(0)
        if site=='@':
            sites.append(1)
    df['Home/Away'] = sites
    return df
