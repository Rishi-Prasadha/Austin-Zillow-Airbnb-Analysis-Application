# Import statements 

import fire
import sys
import questionary
import pandas as pd
from pathlib import Path

airbnb_data = pd.DataFrame(Path("../../britt/listings.csv"))
clean_airbnb_df = airbnb_df.loc[:, ('id', 'host_neighbourhood', 'neighbourhood_cleansed', 'latitude', 'longitude', 'room_type', 'accommodates', 'bedrooms', 'bathrooms_text', 'price', 'review_scores_rating')]
values = ['Private room', 'Shared room', 'Hotel room']
clean_airbnb_df = clean_airbnb_df[clean_airbnb_df.room_type.isin(values) == False]

def enter_zip():
    zip = questionary.text("Enter the zip code you're interested in staying in:").ask()
    zip = int(zip)
    if len(zip) > 5 or len(zip) < 5:
        print('Error: zip code must be 5 digits long')
        sys.exit()
    elif type(zip) != int:
        print("Error: zip code must be a number integer")
    else:
        included_zipcodes = airbnb_data['neighbourhood_cleansed'].tolist()
        for data in included_zipcodes:
            if zip == data:
                return zip
            else:
                print('Error: the zip code you requested cannot be identified')
                sys.exit()

def get_accomodations():
    num_people = questionary.text("Enter the amount of people coming with you:").ask()
    num_people = int(num_people)
    if type(num_people) != int:
        print("Error: Number of people must be an integer")
        sys.exit()
    else:
        included_people = airbnb_data['accommodates'].tolist()
        for data in included_people:
            if num_people == data:
                return num_people
            else:
                print("Error: The number of people is not supported by any listing")
                sys.exit()


def get_beds():
    num_beds = questionary.text("Enter the amount of bedrooms:").ask()
    num_beds = int(num_beds)
    if type(num_beds) != int:
        print("Error: Number of people must be an integer")
        sys.exit()
    else:
        included_bed = airbnb_data['bedrooms'].tolist()
        for data in included_bed:
            if num_beds == data:
                return num_beds
            else:
                print("Error: The number of people is not supported by any listing")
                sys.exit()
    