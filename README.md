# CSE314 SP23 PROJECT: Sports Group

Our project's general focus is on the effects of jetlag, although this is something that has, to some extent, been analyzed in other data projects. In order to differentiate our project from these other analyses, our focus will be on segregating "jetlag" into two groups: jetlag induced by traveling east and jetlag induced by traveling west.

This focus is motivated by research which has shown it is more difficult for the human body to travel east than west. Thus, whether it be a team coach, player, trainer, fan, sports bettor, or other stakeholder in the process of putting on an NFL game, knowing how a team will be affected by a certain type of travel is imperative. At an even more focused level, we are interested in knowing which positional groups (i.e., defensive backs, quarterbacks, receivers, etc.) are most affected by this travel. For the scope of this project, we will primarily focus on quarterback play.

Methodlogy:
- We will examine datasets from the 2022 NFL season for various quarterbacks, with the ability to use our web-scraping functions to acquire data on other position groups and teams as needed.

Deliverables:
- Datasets available for general use as well as our insights (if any) from the projecting done later in this project.

Notes:
- This repository was initially built from the sp23-assignments repository in wustl-data (in order to streamline access to poetry and other python modules). We have tried our best to delete all holdover modules and scripts from that repo that are not relevant for our project, but some may still exist.

- IMPORTANT: To run 'mkdocs serve,' our project currently requires you to run `cd my-project`. We are attempting to free up this functionality such that you don't have to cd into a directory, but those updates will roll out as this project progresses.

Part 1 Documentation: 
- The majority of our data for this project up to this point has been sourced from https://www.pro-football-reference.com, an all encompassing NFL statistical database. Our group made API calls to accumulate targeted data from this website and used the results of the calls to add to an aggregate dataframe. Additonally, longitude and latitude data was manually scraped to determine the location of all NFL stadiums to be used in travel distance calculations later on. 
- pfr_scraping_methods.py: As of now 'retrieve_team_data' is not in use as we are starting small with the amount of data being used. Nonetheless, this method scrapes a wide variety of game data for a parametrized team and year utilizing the web scraping tool BeautifulSoup. The `fix_name` function is currently used in the `retrieve_player_data` function in order to make it more user-friendly such that capitalization of a player's name will not cause the method to fail. The `retrieve_player_data` method scrapes a wide variety of stats on a parametrized player and year utilizing the web scraping tool BeautifulSoup. Finally, `clean_and_normalize_dataset` cleans and normalizes the dataset by turning home and away indication to a binary int variable and by appending a distance traveled column. 
- dataset_management_methods.py: `save` takes a parameter DataFrame and saves it as a .csv. `load` takes a parameter csv (either by local path or url) and returns it as a DataFrame. `calculate_distance` calculates travel distance in miles between the home stadiums of two teams.

Data Normalization/Cleaning:
- In our `retrieve_player_data` function, we decided to drop columns from the initial dataframe constructed from the BeautifulSoup html data because most of the columns were not relevant to our project. We kept only the columns for the week, opponent, whether the game was home or away, and quarterback rating. As mentioned in the previous section, we created a `clean_and_normalize` dataset that encoded the home/away variable, updated columns labels to be more practical, and made sure our dataset was 3NF.

Groups:
- Tom/Sahil: worked on writing functions for scraping and storing the data
- William/Constin: worked on creating our mkdocs server and implementing mkdocs throughout the assignment
- Willem/Rohan: helped write functions for cleaning/normalizing the data as well as with the mkdocs and README

