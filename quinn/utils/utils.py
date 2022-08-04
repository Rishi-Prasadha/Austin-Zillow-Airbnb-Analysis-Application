import fire
import sys
import questionary
import pandas as pd
from pathlib import Path

airbnb_data = pd.read_csv(Path("../britt/listings.csv"))
clean_airbnb_df = airbnb_data.loc[:, ('id', 'host_neighbourhood', 'neighbourhood_cleansed', 'latitude', 'longitude', 'room_type', 'accommodates', 'bedrooms', 'bathrooms_text', 'price', 'review_scores_rating')]
values = ['Private room', 'Shared room', 'Hotel room']
clean_airbnb_df = clean_airbnb_df[clean_airbnb_df.room_type.isin(values) == False]

def enter_zip():
    zip = questionary.text('Enter the zip code for the neighborhood you would like to research').ask()
    zip = int(zip)
    if len(str(zip)) > 5 or len(str(zip)) < 5:
        print(f'The zip code must be 5 digits long')
        sys.exit()
    elif type(zip) != int:
        print(f'The zip code must be an integer')
        sys.exit()
    else:
        included_zipcodes = clean_airbnb_df['neighbourhood_cleansed'].tolist()
        for data in included_zipcodes:
            if zip == int(data):
                return zip
            else:
                print('The zip you requested cannot be found')
                sys.exit()

# Need to check and see if zip is part of df if not we need to print error

def get_accommodations():
    num_people = questionary.text('Enter the amount of people you are looking to accommodate?').ask()
    num_people = int(num_people)
    if type(num_people) != int:
        print(f'The number of people must be an integer')
        sys.exit()
    else:
        included_people = clean_airbnb_df['accommodates'].tolist()
        for data in included_people:
            if num_people == data:
                return num_people
            else:
                print(f'There are no listings that meet this requirement')
                sys.exit()


def get_beds():
    num_beds = questionary.select('How many bedrooms are you looking for?')
    num_beds = int(num_beds)
    if type(num_beds) != int:
        print(f'The number of beds must be an integer')
        sys.exit()
    else:
        included_bed = clean_airbnb_df['bedrooms'].tolist()
        for data in included_bed:
            if num_beds == data:
                return num_beds
            else:
                print(f'There are no listings that meet this requirement')
                sys.exit()

def get_nights():
    nights = questionary.text('How many nights would you like to stay?').ask()
    return nights
