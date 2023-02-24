import pandas as pd
import requests
import os
from dotenv import load_dotenv
import lxml

year = 2022
table_label = 'games'
url = f'https://www.pro-football-reference.com/teams/sea/{year}.htm#{table_label}'
html = urlopen(url)
