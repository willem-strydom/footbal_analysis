import pandas as pd
import requests
import os
from dotenv import load_dotenv
import lxml

load_dotenv()


def table_from_url(table_number:int, url:str) -> pd.DataFrame:
    df = pd.read_html(url)[table_number]
    # print(df)
    return df
#maybe create a function later that would allow you to pass in a table title, convert that title
#to an index, and then use that index to get the table from the url

url = "https://www.pro-football-reference.com/teams/sea/2022/gamelog/#all_gamelog2022"
table_number = 0

df = table_from_url(0,url)
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df)


