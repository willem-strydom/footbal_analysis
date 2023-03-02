# CSE314 SP23 PROJECT: Sports Group

Our project's general focus is on the effects of jetlag, although this is something that has, to some extent, been analyzed in other data projects. In order to differentiate our project from these other analyses, our focus will be on segregating "jetlag" into two groups: jetlag induced by traveling east and jetlag induced by traveling west.

This focus is motivated by research which has shown it is more difficult for the human body to travel east than west. Thus, whether it be a team coach, player, trainer, fan, sports bettor, or other stakeholder in the process of putting on an NFL game, knowing how a team will be affected by a certain type of travel is imperative. At an even more focused level, we are interested in knowing which positional groups (i.e., defensive backs, quarterbacks, receivers, etc.) are most affected by this travel -- as knowing this information would, as referenced earlier, improve informational asymmetries for stakeholders (i.e., make stakeholders more informed about the team and what they can expect from them). 

Methodlogy:
- We will examine datasets from a myriad of NFL games. These datasets will primarily include tables compiled using APIs.
  -> No individual dataset contains all the information we need, so the dataset we eventually manipulate will be unique to our problem.
  -> We will fill in missing and incomplete data according to specific rules, which we will eventually list in this README.

Deliverables:
- Will update this when determined. Will most likely post the dataset somewhere, along with relevant methods, to be used for individual projects.

Notes:
- This repository was initially built from the sp23-assignments repository in wustl-data (in order to streamline access to poetry and other python modules). All branches besides 'main' have been deleted, as they are not germane to this project.

Part 1 Documentation: 
- The majority of our data for this project up to this point has been sourced from https://www.pro-football-reference.com, an all encompassing NFL statistical database. Our group made API calls to accumulate targeted data from this website and used the results of the calls to add to an aggregate dataframe. Additonally, longitude and latitude data was manually scraped to determine the location of all NFL stadiums to be used in travel distance calculations later on. 
- pfr_scraping_methods.py: As of now 'retrieve_team_data' is not in use as we are starting small with the amount of data being used. Nonetheless, this method scrapes a wide variety of game data for a parametrized team and year utilizing the web scraping tool beautifulsoup4. Similarly, 'fix_name' is also currently not in use, but takes in a player's full name and returns that name as a list split into capitalized first and/or middle and/or last name(s). The 'retrieve_player_data' method scrapes a wide variety of stats on a parametrized player and year utilizing the web scraping tool beautifulsoup4. Finally, 'clean_and_normalize_dataset' cleans and normalizes the dataset by turning home and away indication to a binary variable and by appending a distance traveled column. 
- dataset_management_methods.py: 'save' takes a parameter DataFrame and saves it as a .csv. 'load' takes a parameter csv (either by local path or url) and returns it as a DataFrame. 'calculate_distance' calculates travel distance in miles between the home stadiums of two teams.


