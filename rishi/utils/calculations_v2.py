import fire
import sys
import questionary
import pandas as pd
import numpy as np
from pathlib import Path

airbnb_data = pd.read_csv(Path("../britt/listings.csv"))
clean_airbnb_df = airbnb_data.loc[:, ('id', 'host_neighbourhood', 'neighbourhood_cleansed', 'latitude', 'longitude', 'room_type', 'accommodates', 'bedrooms', 'bathrooms_text', 'price', 'review_scores_rating')]
values = ['Private room', 'Shared room', 'Hotel room']
clean_airbnb_df = clean_airbnb_df[clean_airbnb_df.room_type.isin(values) == False]


def calculations(zip, bedrooms, accommodate):
    filter1_df = airbnb_data[airbnb_data['neighbourhood_cleansed'] == zip]
    print(filter1_df)
    filter2_df = filter1_df[filter1_df['bedrooms'] == bedrooms]
    print(filter2_df)
    filter3_df = filter2_df[filter2_df['accommodates'] == accommodate]
    print(filter3_df)

    print(filter3_df['price'].replace('$',''))
    # std = filter3_df['price'].replace('$','').stdev()

    # if average.empty or std.empty:
    #     print("Error: No Airbnbs match with your search criteria, please try again later")
    #     sys.exit()
    # else:
    #     return average, std
    
