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
    """
    gets datafrom from pro football refernce
    args:
        team_abbr (string): abbreviation accourding to pro football reference, may be different than nfl's usage
        year (int): year?
    returns:
        pandas dataframe
    """
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

#alters name format to make string easier to parse for url
def fix_name(full_name : str):
    """
    converts name to appropriate query value
    args:
        fulll_name: player name
    returns:
        name of player
    """
    new_name = full_name.split()
    fixed_name = []
    for name in new_name:
        lowercase = name.lower()
        capitalized = lowercase.capitalize()
        fixed_name.append(capitalized)
    return fixed_name

def retrieve_player_data(player_full_name : str, year : int) -> pd.DataFrame():
    """returns stats for a given player
    args:
        player_full_name (string): name of player
        year (int): year
    returns:
        pandas DataFrame

    """
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
    player_data = player_data[['Date','','Opp','Rate']]
    return player_data

def clean_and_normalize_dataset(df : pd.DataFrame, team_abbr : str) -> pd.DataFrame:
    """returns a cleaned and normalized dataset for a given player
    args:
        df (pd.DataFrame): dataframe of player data
    returns:
        pandas DataFrame

    """
    distances = [dmm.calculate_distance(team_abbr, opponent) for opponent in df['Opp']]
    df['Miles Traveled'] = distances
    if team_abbr == 'SEA':
        df.loc[9, 'Miles Traveled'] = dmm.calculate_distance('SEA', 'GER')
    df = df.rename(columns={"":"Home/Away"})
    sites = []
    for site in df['Home/Away']:
        if site=='':
            sites.append(0)
        if site=='@':
            sites.append(1)
    df['Home/Away'] = sites
    return df

#our project is focused on the 2022 season, but we've added this year functionality to make the function more
#user-friendly
#THESE TWO FUNCTIONS ARE ADDITIONAL FEATURES WE'RE CURRENTLY WORKING ON THAT WILL BE HELPFUL FOR PART 2
def get_top50_quarterbacks(year : int) -> list:
    #scrape the list of quarterbacks from https://www.pro-football-reference.com/years/2022/passing.htm
    url = f'https://www.pro-football-reference.com/years/{year}/passing.htm'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, features="lxml")
    headers = [th.getText() for th in soup.findAll('tr')[0].findAll('th')]
    # print(headers)
    rows = soup.findAll('tr', class_ = lambda table_rows: table_rows != "thead")
    player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(1,51)]
    quarterback_names = [x[0] for x in player_stats]
    remove_asterisks = [name.replace('*','') for name in quarterback_names]
    remove_pluses = [name.replace('+','') for name in remove_asterisks]
    updated_qb_names = remove_pluses
    return updated_qb_names

def concatenate_dataframes(qb_names : list) -> pd.DataFrame():
    empty_list = []
    for quarterback in qb_names:
        qb = retrieve_player_data(quarterback, 2022)
        updated_qb = clean_and_normalize_dataset(qb)
        updated_qb['QB Name'] = quarterback
        empty_list.append(updated_qb)
    final_dataframe = pd.concat(empty_list)
    #passing in a list of quarterbacks from get_all_quarterbacks
    #create an empty list
    #for each quarterback, run retrieve_player_data and clean_and_normalize_dataset
        #add a column where every row in that column is the quarterback name
        #append the dataframes to an empty list
    #use pd.concat to "merge" the dataframes together; takes in a list of dataframes (i.e., list of quarterback dataframes)
    return final_dataframe
# test = get_top50_quarterbacks(2022)
# print(concatenate_dataframes(test))
