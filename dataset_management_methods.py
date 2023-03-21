import pandas as pd
# import pfr_scraping_methods
import json
import geopy.distance

def save(dataset : pd.DataFrame, player : str):
    """save a pd df to a csv

    args:
        dataset (pd.DataFrame): pandas DataFrame
    returns:
        none
    """
    dataset.to_csv(f"expected_data/{player}.csv")

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
        "ARI" : (33.5279053111993, -112.26248802923699),
        "ATL" : (33.75658104611166, -84.4012431938295),
        "BAL" : (39.278055986939314, -76.62271129536873),
        "BUF" : (42.77406838630884, -78.78686792299308),
        "CAR" : (35.225894591145675, -80.85296123497584),
        "CHI" : (41.862433355130726, -87.61668018093484),
        "CIN" : (39.09558815127463, -84.51609417697091),
        "CLE" : (41.50612431804717, -81.69956546223561),
        "DAL" : (32.747394617747304, -97.09449118126838),
        "DEN" : (39.74397867677901, -105.02009065354534),
        "DET" : (42.340040741565296, -83.04558433621338),
        "GNB" : (44.501421493860505, -88.0622361676567),
        "HOU" : (29.684780528466597, -95.41076891897495),
        "IND" : (39.76016855021095, -86.16385742101808),
        "JAX" : (30.32402341109306, -81.63738223023354),
        "KAN" : (39.049006132734625, -94.48390946991661),
        "LVR" : (36.090922613634746, -115.1832957717522),
        "LAC" : (33.953519638164856, -118.33854176452057),
        "LAR" : (33.953519638164856, -118.33854176452057),
        "MIA" : (25.958414687460127, -80.2386036040462),
        "MIN" : (44.973707804914966, -93.25744996631974),
        "NWE" : (42.09099582857695, -71.26437365223678),
        "NOR" : (29.951113428255248, -90.08144686349743),
        "NYG" : (40.81357230213098, -74.07450097583455),
        "NYJ" : (40.81357230213098, -74.07450097583455),
        "PHI" : (39.90141485982268, -75.16749146746251),
        "PIT" : (40.44679727974751, -80.01581448820603),
        "SFO" : (37.40337855622536, -121.96939160572268),
        "SEA" : (47.595148229165446, -122.33209920631144),
        "TAM" : (27.975937833578584, -82.50335871624291),
        "TEN" : (36.16659318662702, -86.77130368128294),
        "WAS" : (38.907777053902784, -76.86463498137742),
        "GER" : (48.21887120658412, 11.624723311594915),
        "MEX" : (19.30293, -99.15054),
        "LON" : (51.60433879666974, -0.06622593043569701)
    }
    coord1 = coordinates[team1]
    coord2 = coordinates[team2]
    return geopy.distance.geodesic(coord1, coord2).miles