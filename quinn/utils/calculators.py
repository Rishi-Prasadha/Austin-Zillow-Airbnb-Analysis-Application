import pandas as pd
import fire
import questionary
import sys
import pathlib as Path

airbnb_data = read_csv()

def avg_price(zip, bed, bath):
    filter1_df = airbnb_data[zip]
    filter2_df = filter1_df[bed]
    filter3_df = filter2_df[bath]
    average = filter3_df['price'].mean()

def std(zip, bed, bath):
    filter1_df = airbnb_data[zip]
    filter2_df = filter1_df[bed]
    filter3_df = filter2_df[bath]
    average = filter3_df['price'].std()

