# Welcome to The Sports Group


<!-- 
## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit. -->

## pfr_scraping_methods.

* This module contains data collection methods to scrape data from [https://www.pro-football-reference.com](https://www.pro-football-reference.com)
* `retrieve_team_data [team_abbr : str, year : int]` - this method scrapes a wide variety of game data for a parametrized team and year, returns a DataFrame.
* `fix_name [full_name : str]` - takes in a player's full name and returns that name as a list split into capitalized first and/or middle and/or last name(s), returns a string.
* `retrieve_player_data [player_full_name : str, year : int]` - scrapes a wide variety of stats on a parametrized player and year, returns a DataFrame
* `clean_and_normalize_dataset [df : pd.DataFrame]` - cleans and normalizes the dataset by turning home and away indication to a binary variable and by appending a distance traveled column, returns a DataFrame


## dataset_management_methods

* this module contains methods to help create new variables from, store, and retrieve data within our project
* `save [dataset : pd.DataFrame]` - takes a parameter DataFrame and saves it as a .csv, no return value
* `load [path : str]` - takes a parameter csv (either by local path or url) and returns it as a DataFrame
* `calculate_distance [team1 : str, team2 : str]` - calculates travel distance in miles between the home stadiums of two teams, returns a float



<!-- ## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files. -->



<!-- ::: workspaces/sports-group/dataset_management_methods.py -->
  