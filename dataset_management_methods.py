import pandas as pd
import pfr_scraping_methods
import json
import geopy.distance

def save(dataset : pd.DataFrame):
    """save a pd df to a csv

    args:
        dataset (pd.DataFrame): pandas DataFrame
    returns:
        none
    """
    dataset.to_csv("data/fake_records.csv")

def load(path : str) -> pd.DataFrame:
    """loads a csv file to pandass DataFrame
    args:
        path: file path to csv file
    returns:
    (pd.DataFrame): pandas DataFrame
    """
    dataframe = pd.read_csv(path)
    return dataframe


def calculate_distance(team1 : str, team2 : str) -> float:
    """calculates travel distance in miles between the home statium of two teams
    args:
        team1 (string): full name of team
        team2 (string): full name of team
    returns:
        (float): distance between teams in miles
    """
    coordinates = {
        "Arizona Cardinals" : (33.5279053111993, -112.26248802923699),
        "Atlanta Falcons" : (33.75658104611166, -84.4012431938295),
        "Baltimore Ravens" : (39.278055986939314, -76.62271129536873),
        "Buffalo Bills" : (42.77406838630884, -78.78686792299308),
        "Carolina Panthers" : (35.225894591145675, -80.85296123497584),
        "Chicago Bears" : (41.862433355130726, -87.61668018093484),
        "Cincinnati Bengals" : (39.09558815127463, -84.51609417697091),
        "Cleveland Browns" : (41.50612431804717, -81.69956546223561),
        "Dallas Cowboys" : (32.747394617747304, -97.09449118126838),
        "Denver Broncos" : (39.74397867677901, -105.02009065354534),
        "Detroit Lions" : (42.340040741565296, -83.04558433621338),
        "Green Bay Packers" : (44.501421493860505, -88.0622361676567),
        "Houston Texans" : (29.684780528466597, -95.41076891897495),
        "Indianapolis Colts" : (39.76016855021095, -86.16385742101808),
        "Jacksonville Jaguars" : (30.32402341109306, -81.63738223023354),
        "Kansas City Chiefs" : (39.049006132734625, -94.48390946991661),
        "Las Vegas Raiders" : (36.090922613634746, -115.1832957717522),
        "Los Angeles Chargers" : (33.953519638164856, -118.33854176452057),
        "Los Angeles Rams" : (33.953519638164856, -118.33854176452057),
        "Miami Dolphins" : (25.958414687460127, -80.2386036040462),
        "Minnesota Vikings" : (44.973707804914966, -93.25744996631974),
        "New England Patriots" : (42.09099582857695, -71.26437365223678),
        "New Orleans Saints" : (29.951113428255248, -90.08144686349743),
        "New York Giants" : (40.81357230213098, -74.07450097583455),
        "New York Jets" : (40.81357230213098, -74.07450097583455),
        "Philadelphia Eagles" : (39.90141485982268, -75.16749146746251),
        "Pittsburgh Steelers" : (40.44679727974751, -80.01581448820603),
        "San Francisco 49ers" : (37.40337855622536, -121.96939160572268),
        "Seattle Seahawks" : (47.595148229165446, -122.33209920631144),
        "Tampa Bay Buccaneers" : (27.975937833578584, -82.50335871624291),
        "Tennessee Titans" : (36.16659318662702, -86.77130368128294),
        "Washington Commanders" : (38.907777053902784, -76.86463498137742)
    }
    coord1 = coordinates[team1]
    coord2 = coordinates[team2]
    return geopy.distance.geodesic(coord1, coord2).miles