#workflow overview
import pandas as pd
import requests
import os
from dotenv import load_dotenv
import lxml
from bs4 import BeautifulSoup
import pfr_scraping_methods as pfr
import dataset_management_methods as dmm

#these are examples of ways you could call these functions to get player data
#each player data dataframe is normalized to 3NF individually

geno = pfr.retrieve_player_data('geno smith', 2022)
geno_updated = pfr.clean_and_normalize_dataset(geno, 'SEA')
dmm.save(geno_updated, 'geno')

tlaw = pfr.retrieve_player_data('trevor lawrence', 2022)
tlaw_updated = pfr.clean_and_normalize_dataset(tlaw, 'JAX')
dmm.save(tlaw_updated, 'tlaw')

mahomes = pfr.retrieve_player_data('PATRICK MAHOMES', 2022)
mahomes_updated = pfr.clean_and_normalize_dataset(mahomes, 'KAN')
dmm.save(mahomes_updated, 'mahomes')





