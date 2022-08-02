import pandas as pd
import fire
import questionary
import sys
from pathlib import Path

airbnb_data = pd.DataFrame(Path('..\..\britt\listings.csv'))
# clean_airbnb_df = airbnb_data.loc[:, ('id', 'host_neighbourhood', 'neighbourhood_cleansed', 'latitude', 'longitude', 'room_type', 'accommodates', 'bedrooms', 'bathrooms_text', 'price', 'review_scores_rating')]
# values = ['Private room', 'Shared room', 'Hotel room']
# clean_airbnb_df = clean_airbnb_df[clean_airbnb_df.room_type.isin(values) == False]

def calculations(zip, bedrooms, accomodate):
    filter1_df = airbnb_data[airbnb_data['neighbourhood_cleansed'] == zip]
    filter2_df = filter1_df[filter1_df['bedrooms'] == bedrooms]
    filter3_df = filter2_df[filter2_df['accomodates'] == accomodate]
    average = filter3_df['price'].mean()
    stddev = filter3_df['price'].stdev()

    if average.empty or stddev.empty:
        print(f'There are no listings that match your search criteria')
        sys.exit()
    else:
        return average, stddev
