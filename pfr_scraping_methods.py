import pandas as pd
import requests
import os
from dotenv import load_dotenv
import lxml
from bs4 import BeautifulSoup
from dataset_management_methods import calculate_distance

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
    need_01 = ['Joe Burrow', 'Dak Prescott', 'Marcus Mariota', 'Mike White', 'Tyler Huntley']
    need_02 = ['Josh Allen', 'Derek Carr', 'Davis Mills']
    need_05 = ['Daniel Jones', 'Mac Jones']
    #edge cases
    name = " ".join(first_and_last)
    if name in need_01:
       unique_player_string = first_and_last[1][:4] + first_and_last[0][:2] + '01'
    else:
        if name in need_02:
            unique_player_string = first_and_last[1][:4] + first_and_last[0][:2] + '02'
        else:
            if name in need_05:
                unique_player_string = first_and_last[1][:4] + first_and_last[0][:2] + '05'
            else:
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
    #need to include the edge case of the Bengals/Bills cancelling their week 17 game
    copy = df.copy()
    mask = copy.index<16
    if team_abbr == 'CIN':
        copy = copy.loc[mask, :]
    if team_abbr == 'BUF':
        copy = copy.loc[mask, :]
    distances = [calculate_distance(team_abbr, opponent) for opponent in copy['Opp']]
    copy.loc[:, 'Miles Traveled'] = distances
    df = copy
    #edge cases
    if (team_abbr == 'SEA'):
        df.loc[9, 'Miles Traveled'] = calculate_distance('SEA', 'GER')
    if (team_abbr == 'TAM'):
        df.loc[9, 'Miles Traveled'] = calculate_distance('TAM', 'GER')
    if (team_abbr == 'NOR'):
        df.loc[3, 'Miles Traveled'] = calculate_distance('NOR', 'LON')
    if (team_abbr == 'MIN'):
        df.loc[3, 'Miles Traveled'] = calculate_distance('MIN', 'LON')  
    if (team_abbr == 'GNB'):
        df.loc[4, 'Miles Traveled'] = calculate_distance('GNB', 'LON')
    if (team_abbr == 'NYG'):
        df.loc[4, 'Miles Traveled'] = calculate_distance('NYG', 'LON')
    if (team_abbr == 'DEN'):
        df.loc[7, 'Miles Traveled'] = calculate_distance('DEN', 'MEX')
    if (team_abbr == 'JAX'):
        df.loc[7, 'Miles Traveled'] = calculate_distance('JAX', 'MEX')
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
def get_top25_quarterbacks(year : int) -> list:
    """returns a list of (quarterback, team_abbr) tuples
    args:
        year (int): a specific NFL season; for our project, this will be 2022
    returns:
        pandas DataFrame

    """
    #scrape the list of quarterbacks from https://www.pro-football-reference.com/years/2022/passing.htm
    url = f'https://www.pro-football-reference.com/years/{year}/passing.htm'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, features="lxml")
    headers = [th.getText() for th in soup.findAll('tr')[0].findAll('th')]
    # print(headers)
    rows = soup.findAll('tr', class_ = lambda table_rows: table_rows != "thead")
    player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(1,26)]
    quarterback_names = [x[0] for x in player_stats]
    remove_asterisks = [name.replace('*','') for name in quarterback_names]
    remove_pluses = [name.replace('+','') for name in remove_asterisks]
    updated_qb_names = remove_pluses
    team_abbreviations = [x[1] for x in player_stats]
    merged_list = [(updated_qb_names[i], team_abbreviations[i]) for i in range(0, len(updated_qb_names))]
    return merged_list

# print(get_top50_quarterbacks(2022))

#For part 2 --> will need to add all the international games to the dict
def concatenate_dataframes(qb_names_and_abbreviations : list) -> pd.DataFrame():
    """returns a dataframe with all qb information concatenated together
    args:
        qb_names_and_abbreviations (list): a list of (quarterback, team_abbr) tuples 
    returns:
        pandas DataFrame

    """
    empty_list = []
    for quarterback, team_abbrevation in qb_names_and_abbreviations:
        qb = retrieve_player_data(quarterback, 2022)
        # print(qb)
        updated_qb = clean_and_normalize_dataset(qb, team_abbrevation)
        # print(updated_qb)
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