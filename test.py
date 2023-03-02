#workflow overview
import pandas as pd
import requests
import os
from dotenv import load_dotenv
import lxml
from bs4 import BeautifulSoup
import pfr_scraping_methods as pfr
import dataset_management_methods as dmm

geno = pfr.retrieve_player_data('geno smith', 2022)
geno_updated = pfr.clean_and_normalize_dataset(geno)
print(geno_updated)






