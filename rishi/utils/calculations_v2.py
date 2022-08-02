import fire
import sys
import questionary
import pandas as pd
from pathlib import Path

airbnb_data = pd.DataFrame(Path("../Resources/austin_airbnb_data.csv"))

def ave(zip, bed, bath):
    filter1_df = airbnb_data[zip]
    filter2_df = filter1_df[bed]
    filter3_df = filter2_df[bath]
    average = filter3_df['price'].mean()

def stddev(zip, bed, bath):
    filter1_df = airbnb_data[zip]
    filter2_df = filter1_df[bed]
    filter3_df = filter2_df[bath]
    average = filter3_df['price'].std()