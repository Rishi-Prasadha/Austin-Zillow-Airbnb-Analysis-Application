import fire
import sys
import questionary
import pandas as pd
from pathlib import Path

airbnb_data = pd.DataFrame(Path("../../britt/listings.csv"))

def ave(zip, bedrooms, accommodate):
    filter1_df = airbnb_data[airbnb_data['neighbourhood_cleansed'] == zip]
    filter2_df = filter1_df[filter1_df['bedrooms'] == bedrooms]
    filter3_df = filter2_df[filter2_df['accommodates'] == accommodate]
    average = filter3_df['price'].mean()
    
    if average.empty:
        print("Error: No Airbnbs match with your search criteria, please try again later")
        sys.exit()
    else:
        return stddev
    


def stddev(zip, bedrooms, accommodate):
    filter1_df = airbnb_data[airbnb_data['neighbourhood_cleansed'] == zip]
    filter2_df = filter1_df[filter1_df['bedrooms'] == bedrooms]
    filter3_df = filter2_df[filter2_df['accommodates'] == accommodate]
    average = filter3_df['price'].mean()

    if stddev.empty:
        print("Error: No Airbnbs match with your search criteria, please try again later")
        sys.exit()
    else:
        return stddev
