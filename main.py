import pandas as pd
import requests
import os
from dotenv import load_dotenv
import kaggle

load_dotenv()

url = "https://www.pro-football-reference.com/teams/sea/2022/gamelog/#all_gamelog2022"
df = pd.read_html(url)[0]